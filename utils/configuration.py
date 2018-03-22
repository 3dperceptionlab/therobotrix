import json

class Configuration():

    def __init__(self):

        self.m_unrealengine_host = "challenger.dtic.ua.es"
        self.m_unrealengine_port = 9000
        
        self.m_sequence_filename = "../data/sequence.json"

        self.m_camera_fx = 320.0
        self.m_camera_cx = 320.0
        self.m_camera_fy = 320
        self.m_camera_cy = 240
        self.m_camera_fov = 90.0
        self.m_camera_depthmin = 0.0
        self.m_camera_depthmax = 7.0

        self.m_segmentation_mapping = 'color_mapping.txt'
        self.m_segmentation_categories = 'object_categories.json'

    def __repr__(self):

        return "Configuration(UE - Host: " + \
                self.m_unrealengine_host + \
                ", UE - Port: " + \
                str(self.m_unrealengine_port) + \
                ")"

    def load(self, filename):

        print("Reading configuration file " + filename)

        with open(filename, 'r') as stream:

            config_data = json.load(stream)

            self.m_unrealengine_host = config_data["unrealengine"]["host"]
            self.m_unrealengine_port = config_data["unrealengine"]["port"]

            self.m_sequence_filename = config_data["scene"]["filename"]
        
            self.m_camera_fx = config_data["camera"]["fx"]
            self.m_camera_cx = config_data["camera"]["cx"]
            self.m_camera_fy = config_data["camera"]["fy"]
            self.m_camera_cy = config_data["camera"]["cy"]
            self.m_camera_fov = config_data["camera"]["fov"]
            self.m_camera_depthmin = config_data["camera"]["depthmin"]
            self.m_camera_depthmax = config_data["camera"]["depthmax"]

            self.m_segmentation_mapping = config_data["segmentation"]["mapping"]
            self.m_segmentation_categories = config_data["segmentation"]["categories"]
