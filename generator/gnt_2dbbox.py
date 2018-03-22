import numpy as np
from PIL import Image, ImageDraw
import sys
import xml.etree.cElementTree as ET

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

def compute_bbox(mask, color):

    binary_mask_ = np.zeros((mask.shape[0], mask.shape[1]))
    region_ = match_color(mask, [color.m_r, color.m_g, color.m_b], tolerance=3)
    binary_mask_[region_] = 1.0

    rows_ = np.any(binary_mask_, axis=1)
    cols_ = np.any(binary_mask_, axis=0)

    r_min_ = -1
    r_max_ = -1
    c_min_ = -1
    c_max_ = -1

    if (np.any(rows_) and np.any(cols_)):
        r_min_, r_max_ = np.where(rows_)[0][[0, -1]]
        c_min_, c_max_ = np.where(cols_)[0][[0, -1]]

    return r_min_, c_min_, r_max_, c_max_

def generate_2d_bbox(img, mask, objects, filename):

    bboxes_ = np.zeros_like(mask)

    base_ = Image.fromarray(img)
    xml_annotation_ = ET.Element("annotation")
    xml_segmented_ = ET.SubElement(xml_annotation_, "segmented").text = "0"
    xml_size_ = ET.SubElement(xml_annotation_, "size")
    xml_width_ = ET.SubElement(xml_size_, "width").text = str(mask.shape[1])
    xml_height_ = ET.SubElement(xml_size_, "height").text = str(mask.shape[0])
    xml_depth_ = ET.SubElement(xml_size_, "depth").text = "3"

    for i_obj in objects.keys():

        if objects[i_obj].m_class.m_detection_class == "none":
            continue

        r_min_, c_min_, r_max_, c_max_ = compute_bbox(mask, objects[i_obj].m_instance_color)

        if r_min_ == -1 or c_min_ == -1 or r_max_ == -1 or c_max_ == -1:
            continue

        if objects[i_obj].m_class != "none":
            color_ = objects[i_obj].m_class.m_color
            rgb_color_ = [color_.m_r, color_.m_g, color_.m_b, 128]
            bboxes_[r_min_:r_max_, c_min_:c_max_] = rgb_color_

            bbox_base_ = np.array(Image.new('RGBA', base_.size, (255,255,255,0)))
            bbox_base_[r_min_:r_max_, c_min_:c_max_] = rgb_color_
            base_ = Image.alpha_composite(base_, Image.fromarray(bbox_base_))

            xml_object_ = ET.SubElement(xml_annotation_, "object")
            ET.SubElement(xml_object_, "name").text = objects[i_obj].m_class.m_name
            ET.SubElement(xml_object_, "pose").text = "Unspecified"
            ET.SubElement(xml_object_, "truncated").text = "0"
            ET.SubElement(xml_object_, "difficult").text = "0"
            xml_bndbox_ = ET.SubElement(xml_object_, "bndbox")
            ET.SubElement(xml_bndbox_, "xmin").text = str(c_min_)
            ET.SubElement(xml_bndbox_, "ymin").text = str(r_min_)
            ET.SubElement(xml_bndbox_, "xmax").text = str(c_max_)
            ET.SubElement(xml_bndbox_, "ymax").text = str(r_max_)

    xml_tree_ = ET.ElementTree(xml_annotation_)
    xml_tree_.write(filename + ".xml")
    img_bboxes_ = Image.fromarray(bboxes_)
    img_bboxes_.save(filename)
    base_.save(filename)
