from color import Color
from objectclass import ObjectClass

class SceneObject():

    def __init__(self):

        self.m_instance = "none"
        self.m_instance_color = Color()
        self.m_class = ObjectClass()

    def __repr__(self):

        return "SceneObject(instance: {0}, color: {1}, class: {2})".format(
             self.m_instance,
             self.m_instance_color,
             self.m_class)

    def parse_json(self, sceneObjectJson):

        self.m_instance = sceneObjectJson["instance_name"]
        color_ = Color()
        color_.parse_json(sceneObjectJson["instance_color"])
        self.m_instance_color = color_
        class_ = ObjectClass()
        class_.parse_json(sceneObjectJson["class"])
        self.m_class = class_

    def to_json(self):

        sceneobject_json_ = {}
        sceneobject_json_["instance_name"] = self.m_instance
        sceneobject_json_["instance_color"] = self.m_instance_color.to_json()
        sceneobject_json_["class"] = self.m_class.to_json()
        return sceneobject_json_
