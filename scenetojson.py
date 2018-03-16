import json
from itertools import groupby

FILE_NAME = "scene_0.txt"
SEQUENCE_NAME = "hamburg_seq0_oculus1"

drop_frames = 1
skip_n_frames = 1

with open(FILE_NAME) as f:
    lines_ = f.readlines()
    lines_ = [x.strip('\r\n') for x in lines_]

    frames_ = (list(g) for k, g in groupby(lines_, key=lambda x: x != 'frame') if k)

    sequence = {}
    sequence["name"] = SEQUENCE_NAME
    sequence["frames"] = []

    i = 0
    last_frame_objects_ = {}

    for fr in frames_:

        if i < skip_n_frames:
            i = i + 1
            continue

        frame_ = {}

        # Frame ID
        frame_["id"] = "{:06d}".format(i)

        # Frame timestamp
        frame_["timestamp"] = fr[0].split()[0]

        # Frame camera
        frame_["camera"] = {}
        frame_["camera"]["position"] = {}
        frame_["camera"]["rotation"] = {}

        camera_values_ = fr[1].split()[1:]
        camera_position_ = [x.split('=') for x in camera_values_[0:3]]
        camera_x_ = camera_position_[0][1]
        camera_y_ = camera_position_[1][1]
        camera_z_ = camera_position_[2][1]

        frame_["camera"]["position"]["x"] = camera_x_
        frame_["camera"]["position"]["y"] = camera_y_
        frame_["camera"]["position"]["z"] = camera_z_

        camera_rotation_ = [x.split('=') for x in camera_values_[3:]]
        camera_p_ = camera_rotation_[0][1]
        camera_y_ = camera_rotation_[1][1]
        camera_r_ = camera_rotation_[2][1]

        frame_["camera"]["rotation"]["p"] = camera_p_
        frame_["camera"]["rotation"]["y"] = camera_y_
        frame_["camera"]["rotation"]["r"] = camera_r_

        # Frame objects
        frame_["objects"] = []

        objects_ = fr[2:]

        for obj in objects_:

            print(obj)
            obj_ = obj.split()
            object_ = {}

            # Object name
            object_["name"] = obj_[0]
            print("Processing object {0}...".format(object_["name"]))

            # Object position
            object_["position"] = {}
            object_["rotation"] = {}
            object_values_ = obj_[1:]

            object_position_ = [x.split('=') for x in object_values_[0:3]]
            object_x_ = object_position_[0][1]
            object_y_ = object_position_[1][1]
            object_z_ = object_position_[2][1]

            object_["position"]["x"] = object_x_
            object_["position"]["y"] = object_y_
            object_["position"]["z"] = object_z_

            object_rotation_ = [x.split('=') for x in object_values_[3:]]
            object_p_ = object_rotation_[0][1]
            object_y_ = object_rotation_[1][1]
            object_r_ = object_rotation_[2][1]

            object_["rotation"]["p"] = object_p_
            object_["rotation"]["y"] = object_y_
            object_["rotation"]["r"] = object_r_

            if object_["name"] in last_frame_objects_:
                if last_frame_objects_[object_["name"]]["position"] == object_position_ and last_frame_objects_[object_["name"]]["rotation"] == object_rotation_:
                    print("Object {0} did not move, skipping...".format(object_["name"]))
                    continue
                else:
                    last_frame_objects_[object_["name"]]["position"] = object_position_
                    last_frame_objects_[object_["name"]]["rotation"] = object_rotation_
                    frame_["objects"].append(object_)
            else:
                print("New object, adding to last frame objects...")
                last_frame_objects_[object_["name"]] = {}
                last_frame_objects_[object_["name"]]["position"] = object_position_
                last_frame_objects_[object_["name"]]["rotation"] = object_rotation_
                frame_["objects"].append(object_)

        sequence["frames"].append(frame_)
        print("**** FRAME " + str(i) + " ****")
        print("Timestamp: " + fr[0])
        print("Camera: ")
        print(camera_position_)
        print(camera_rotation_)

        i = i + 1

    print('Total frames: ' + str(len(sequence["frames"])))
    sequence["frames"] = sequence["frames"][::drop_frames]
    print('Frames after keeping every ' + str(drop_frames) + ' is ' + str(len(sequence["frames"])))
    sequence["total_frames"] = len(sequence["frames"])

    with open("data/" + SEQUENCE_NAME + ".json", 'w') as out_f:
        json.dump(sequence, out_f, indent=2)


