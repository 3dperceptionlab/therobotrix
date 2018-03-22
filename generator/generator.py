import numpy as np
import json
import sys

sys.path.append('../')

from PIL import Image

from utils.camera import Camera
from utils.sceneobject import SceneObject
from utils.sequence import Sequence

import gnt_2dbbox as gnt_2dbbox
import gnt_2dclassmask as gnt_2dclassmask
import gnt_cloud as gnt_cloud

SEQUENCE_DIR = "hamburg_seq0_oculus0"
FRAME_START = 0

def main(argv):

    print("Generating data for sequence {0}".format(SEQUENCE_DIR))

    print("Loading camera information...")
    cam_ = Camera()
    cam_.load("../data/" + SEQUENCE_DIR + "/camera.json")
    print(cam_)

    print("Loading sequence information...")
    seq_ = Sequence()
    seq_.load("../data/" + SEQUENCE_DIR + "/sequence.json")
    print(seq_)

    print("Loading object information...")
    objects_ = {}
    objects_json_ = {}
    with open("../data/" + SEQUENCE_DIR + "/objects.json", 'r') as f:
        objects_json_ = json.load(f)

    objects_json_ = objects_json_["objects"]

    for i_objname in objects_json_.keys():

        print("Loading object {0}".format(i_objname))
        obj_ = SceneObject()
        obj_.parse_json(objects_json_[i_objname])
        print(obj_)
        objects_[i_objname] = obj_

    for i in range(seq_.m_total_frames):

        if i < FRAME_START:
            i += 1
            continue

        print("Processing frame {0} out of {1}".format(i, seq_.m_total_frames))
        frame_id_ = seq_.m_frames[i]["id"]

        print("Generating RGB, depth, and mask frames filenames...")
        frame_rgb_name_ = "../data/" + SEQUENCE_DIR + "/rgb/" + frame_id_ + ".png"
        print(frame_rgb_name_)
        frame_depth_name_ = "../data/" + SEQUENCE_DIR + "/depth/" + frame_id_ + ".png"
        print(frame_depth_name_)
        frame_mask_name_ = "../data/" + SEQUENCE_DIR + "/mask/" + frame_id_ + ".png"
        print(frame_mask_name_)

        print("Fetching RGB, depth, and mask images...")
        frame_rgb_img_ = np.asarray(Image.open(frame_rgb_name_))
        frame_depth_img_ = np.asarray(Image.open(frame_depth_name_))
        frame_mask_img_ = np.asarray(Image.open(frame_mask_name_))

        # Generate colored point cloud
        print("Generating colored point cloud...")
        frame_cloud_name_ = "../data/" + SEQUENCE_DIR + "/cloud/" + frame_id_ + ".ply"
        gnt_cloud.generate_cloud(frame_depth_img_, frame_rgb_img_, cam_, frame_cloud_name_)

        # Generate 2D class mask
        print("Generating 2D class mask...")
        frame_2dclassmask_name_ = "../data/" + SEQUENCE_DIR + "/2dclassmask/" + frame_id_ + ".png"
        gnt_2dclassmask.generate_2d_class_mask(frame_mask_img_, objects_, frame_2dclassmask_name_)

		    ## Generate 2D bounding boxes
        print("Generating 2D bounding boxes...")
        frame_2dbbox_name_ = "../data/" + SEQUENCE_DIR + "/2dbbox/" + frame_id_ + ".png"
        gnt_2dbbox.generate_2d_bbox(frame_rgb_img_, frame_mask_img_, objects_, frame_2dbbox_name_)

if __name__ == "__main__":
    main(sys.argv)
