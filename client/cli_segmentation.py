import json
import numpy as np
import re
import cli_utils as utils

class Color(object):
    regexp = re.compile('\(R=(.*),G=(.*),B=(.*),A=(.*)\)')

    def __init__(self, color_str):
        self.color_str = color_str
        match = self.regexp.match(color_str)
        (self.R, self.G, self.B, self.A) = [int(match.group(i)) for i in range(1, 5)]

    def __repr__(self):
        return self.color_str

def get_object_mask(client):

    res = client.request('vget /camera/0/object_mask png')
    
    if res is None:
        return None

    img = utils.read_png(res)
    print 'Read object mask image with shape ' + str(img.shape)
    return img

def match_color(color_image, target_color, tolerance=3):

    match_region = np.ones(color_image.shape[0:2], dtype=bool)
    for c in range(3):
        min_val_ = target_color[c] - tolerance
        max_val_ = target_color[c] + tolerance
        channel_region = (color_image[:, :, c] >= min_val_) & (color_image[:, :, c] <= max_val_)
        match_region &= channel_region

    return match_region

def compute_instance_masks(object_mask, color_mapping, objects):
    instance_masks_ = {}

    for obj in objects:
        color = color_mapping[obj]
        region = match_color(object_mask, [color.R, color.G, color.B], tolerance=3)
        if region.sum() != 0:
            instance_masks_[obj] = region

    return instance_masks_

def generate_object_class_mask(client, object_mask, categories_file, mapping_file):

    per_class_mask_ = object_mask.copy()
    per_class_mask_[:, :, :] = 0

    # Obtain scene object list
    object_list_ = client.request('vget /objects').split(' ')
    print("There are " + str(len(object_list_)) + " objects in this scene...")

    # Get per-instance rendered color mapping
    color_mapping_ = {}
    for object_name in object_list_:
        color_mapping_[object_name] = Color(client.request('vget /object/%s/color' % object_name))

    # Load object categories
    with open(categories_file) as f:
        object_categories_ = json.load(f)
    categories_ = set(object_categories_.values())

    print(categories_)

    # Create color dictionary for category-color mapping
    colors_ = {}
    for category in categories_:
        colors_[category] = [0, 0, 0]

    # Load category colors
    with open(mapping_file) as f:
        lines_ = [x.strip() for x in f.readlines()]
        for line in lines_:
            split_ = line.split()
            category_ = split_[0]
            color_ = [int(split_[1]), int(split_[2]), int(split_[3])]
            colors_[category_] = color_

    # Compute binary mask for each object in the scene
    instance_masks_ = compute_instance_masks(object_mask, color_mapping_, object_list_)
    # Get objects in the current render
    image_objects_ = instance_masks_.keys()
    print image_objects_

    # Generate per-class mask merging all objects with the same category
    for category in categories_:
        mask_ = None
        for obj in image_objects_:
            if object_categories_[obj] == category:
                if mask_ is None:
                    mask_ = instance_masks_[obj]
                else:
                    mask_ += instance_masks_[obj]

        if mask_ is not None:
            per_class_mask_[mask_] = colors_[category]

    return per_class_mask_
