import json
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import time
import sys

import cli_utils as cli_utils

sys.path.append('../')

from utils.camera import Camera
from utils.objectclass import ObjectClass
from utils.color import Color
from utils.configuration import Configuration
from utils.sceneobject import SceneObject
from utils.sequence import Sequence

import utils.ucv as ucv

import cli_rgb as cli_rgb
import cli_depth as cli_dpt
import cli_segmentation as cli_sgm

CONFIG_FILE = "../config/config.json"
FRAME_START = 6762

def main(argv):

    ## Create and load client configuration
    cfg_ = Configuration()
    cfg_.load(CONFIG_FILE)
    print cfg_
    
    ## Create UnrealCV client and connect
    ucv_client_ = ucv.connect_client(cfg_.m_unrealengine_host, cfg_.m_unrealengine_port)

    ## Load sequence configuration file and properties and save description
    seq_ = Sequence()
    seq_.load(cfg_.m_sequence_filename)
    print seq_
    seq_.save("../data/" + seq_.m_name + "/sequence.json")

    ## Generate camera description
    cam_ = Camera()
    cam_.m_fx = cfg_.m_camera_fx
    cam_.m_fy = cfg_.m_camera_fy
    cam_.m_cx = cfg_.m_camera_cx
    cam_.m_cy = cfg_.m_camera_cy
    cam_.m_fov = cfg_.m_camera_fov
    cam_.m_depthmin = cfg_.m_camera_depthmin
    cam_.m_depthmax = cfg_.m_camera_depthmax
    print cam_
    cam_.save("../data/" + seq_.m_name + "/camera.json")

    ## Generate objects description
    object_list_ = ucv_client_.request("vget /objects").split(' ')

    objects_ = {}
    objects_["total_number"] = len(object_list_)
    objects_["objects"] = {}

    print("There are " + str(objects_["total_number"]) + " objects in this scene...")

    ### Load object instance to object class mapping
    instance_class_ = {}
    with open("../config/instance_class.json") as f:
        instance_class_ = json.load(f)

    ### Load class information
    classes_ = {}
    with open("../config/classes.json") as f:
        classes_json_ = json.load(f)
        
        for i_classid in classes_json_.keys():
            obj_class_ = ObjectClass()
            obj_class_.parse_json(classes_json_[i_classid])
            classes_[i_classid] = obj_class_

    ### Describe each object 
    for i_objname in object_list_:

        object_ = SceneObject()
 
        object_.m_instance_name = i_objname
        print("Getting color for {0}".format(i_objname))
        object_color_ = Color(ucv_client_.request("vget /object/{0}/color".format(i_objname)))
        print("Object {0} has color {1}".format(i_objname, object_color_))
        object_.m_instance_color = object_color_

        if i_objname in instance_class_:
            object_.m_class = classes_[instance_class_[i_objname]]
        else:
            object_.m_class = classes_["none"]

        objects_["objects"][i_objname] = object_.to_json()

    with open("../data/" + seq_.m_name + "/objects.json", 'w') as f:
        json.dump(objects_, f, indent=2)

    ## Get frames
    for i in range(seq_.m_total_frames):

        print("Getting frame {0} out of {1}...".format(i, seq_.m_total_frames))

        if i < FRAME_START:
            print("Skipping frame " + str(i))
            continue
        
        frame_ = seq_.m_frames[i]

        frame_id_ = frame_["id"]        
        frame_timestamp_ = frame_["timestamp"]
        frame_camera_ = frame_["camera"]
        frame_objects_ = frame_["objects"]

        print frame_timestamp_
        res_camera_ = ucv.place_camera(ucv_client_, frame_camera_)
        while (res_camera_ is None):
            print("ERROR: Trying to place camera again...")
            ucv_client_.disconnect()
            ucv_client_ = ucv.connect_client(cfg_.m_unrealengine_host, cfg_.m_unrealengine_port)
            res_camera_ = ucv.place_camera(ucv_client_, frame_camera_)

        ucv.place_objects(ucv_client_, frame_objects_)
        
        frame_rgb_ = cli_rgb.get_rgb(ucv_client_)
        while (frame_rgb_ is None):
            print("ERROR: Trying to get RGB frame again...")
            ucv_client_.disconnect()
            ucv_client_ = ucv.connect_client(cfg_.m_unrealengine_host, cfg_.m_unrealengine_port)
            frame_rgb_ = cli_rgb.get_rgb(ucv_client_)

        frame_rgb_im_ = Image.fromarray(frame_rgb_)
        frame_rgb_im_.save("../data/" + seq_.m_name + "/rgb/" + frame_id_ + ".png")
        
        frame_mask_ = cli_sgm.get_object_mask(ucv_client_)
        while (frame_mask_ is None):
            print("ERROR: Trying to get mask frame again...")
            ucv_client_.disconnect()
            ucv_client_ = ucv.connect_client(cfg_.m_unrealengine_host, cfg_.m_unrealengine_port)
            frame_mask_ = cli_sgm.get_object_mask(ucv_client_)

        frame_mask_im_ = Image.fromarray(frame_mask_)
        frame_mask_im_.save("../data/" + seq_.m_name + "/mask/" + frame_id_ + ".png")

        frame_depth_ = cli_dpt.get_depth(ucv_client_)
        while (frame_depth_ is None):
            print("ERROR: Trying to get depth frame again...")
            ucv_client_.disconnect()
            ucv_client_ = ucv.connect_client(cfg_.m_unrealengine_host, cfg_.m_unrealengine_port)
            frame_depth_ = cli_dpt.get_depth(ucv_client_)

        frame_depth_im_ = Image.fromarray(frame_depth_)
        cli_utils.save_16bit_png(frame_depth_, "../data/" + seq_.m_name + "/depth/" + frame_id_ + ".png", cam_.m_depthmin, cam_.m_depthmax)

if __name__ == "__main__":
	main(sys.argv)
