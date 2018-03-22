from color import Color

class ObjectClass():

    def __init__(self):

        self.m_name = "none"
        self.m_semantic_class = "none"
        self.m_color = Color()
        self.m_detection_class = "none"

    def __repr__(self):

        return "Class(name:{0}, semantic:{1}, color:{2}, detection:{3})".format(
            self.m_name,
            self.m_semantic_class,
            self.m_color,
            self.m_detection_class)

    def parse_json(self, classJson):

        self.m_name = classJson["name"]
        self.m_semantic_class = classJson["semantic_class"]
        self.m_color.parse_json(classJson["color"])
        self.m_detection_class = classJson["detection_class"]

    def to_json(self):

        objectclass_json_ = {}
        objectclass_json_["name"] = self.m_name
        objectclass_json_["semantic_class"] = self.m_semantic_class
        objectclass_json_["color"] = self.m_color.to_json()
        objectclass_json_["detection_class"] = self.m_detection_class
        return objectclass_json_
