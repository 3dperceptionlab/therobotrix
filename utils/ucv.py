import unrealcv
import sys

def connect_client(host, port):

    print("Connecting to UnrealCV client...")
    client_ = unrealcv.Client((host, port))
    print("Client created...")
    client_.connect()

    if not client_.isconnected():

        print("Could not connect UnrealCV client with host " + host + ":" + str(port))
        sys.exit()

    else:

        print("Client connected!")
        res = client_.request('vget /unrealcv/status')
        print(res)
        
    return client_

def get_object_list(client):

    object_list_ = client.request("vget /objects").split(' ')
    return object_list_

def place_camera(client, camera):
    
    camera_position_ = camera["position"]
    camera_position_x_ = camera_position_["x"]
    camera_position_y_ = camera_position_["y"]
    camera_position_z_ = camera_position_["z"]
    camera_rotation_ = camera["rotation"]
    camera_rotation_p_ = camera_rotation_["p"]
    camera_rotation_y_ = camera_rotation_["y"]
    camera_rotation_r_ = camera_rotation_["r"]

    print('Setting camera position to ' + camera_position_x_ + ' ' + camera_position_y_ + ' ' + camera_position_z_)
    print('Setting camera rotation to ' + camera_rotation_p_ + ' ' + camera_rotation_y_ + ' ' + camera_rotation_r_)
    # TODO: make robust against errors
    client.request('vset /camera/0/pose '\
            + str(camera_position_x_) + ' ' \
            + str(camera_position_y_) + ' ' \
            + str(camera_position_z_) + ' ' \
            + str(camera_rotation_p_) + ' ' \
            + str(camera_rotation_y_) + ' ' \
            + str(camera_rotation_r_))

def place_objects(client, objects):
    
    for i in range(len(objects)):
        
        object_ = objects[i]

        object_name_ = object_["name"]
        object_position_ = object_["position"]
        object_position_x_ = object_position_["x"]
        object_position_y_ = object_position_["y"]
        object_position_z_ = object_position_["z"]
        object_rotation_ = object_["rotation"]
        object_rotation_p_ = object_rotation_["p"]
        object_rotation_y_ = object_rotation_["y"]
        object_rotation_r_ = object_rotation_["r"]
        
        print('Setting object ' + object_name_ + ' position to '\
                + object_position_x_ + ' ' + object_position_y_ + ' ' + object_position_z_)

	# TODO: make robust against errors
        client.request('vset /object/' + object_name_ + '/location ' \
                + str(object_position_x_) \
                + str(object_position_y_) \
                + str(object_position_z_))
        
        print('Setting object ' + object_name_ + ' rotation to ' + \
                object_rotation_p_ + ' ' + object_rotation_y_ + ' ' + object_rotation_r_)

	# TODO: make robust against errors
        client.request('vset /object/' + object_name_ + '/rotation ' \
                + str(object_rotation_p_) \
                + str(object_rotation_y_) \
                + str(object_rotation_r_))

