import numpy as np
from PIL import Image
import sys

sys.path.append("../")

from utils.color import Color

def match_color(colorImage, targetColor, tolerance=3):

    match_region_ = np.ones(colorImage.shape[0:2], dtype=bool)

    for c in range(3):

        min_val_ = targetColor[c] - tolerance
        max_val_ = targetColor[c] + tolerance
        channel_region_ = (colorImage[:, :, c] >= min_val_) & (colorImage[:, :, c] <= max_val_)
        match_region_ &= channel_region_

    return match_region_

def compute_instance_masks(mask, objects):

    instance_masks_ = {}

    for i_objname in objects.keys():

        color_ = objects[i_objname].m_instance_color

        region_ = match_color(mask, [color_.m_r, color_.m_g, color_.m_b], tolerance=3)

        if region_.sum() != 0:
            instance_masks_[i_objname] = region_

    return instance_masks_

def generate_2d_class_mask(mask, objects, filename):

    per_class_mask_ = mask.copy()
    per_class_mask_[:, :, :] = 0

    # Compute binary mask for each object in the scene
    instance_masks_ = compute_instance_masks(mask, objects)

    # Generate per-class masking
    for i_instancename in instance_masks_.keys():
        mask_ = instance_masks_[i_instancename]
        color_ = objects[i_instancename].m_class.m_color
        rgb_color_ = [color_.m_r, color_.m_g, color_.m_b, 255]
        per_class_mask_[mask_] = rgb_color_

    img_per_class_mask_ = Image.fromarray(per_class_mask_)
    img_per_class_mask_.save(filename)
