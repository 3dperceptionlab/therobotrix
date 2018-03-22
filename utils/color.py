import re

class Color(object):
    regexp = re.compile('\(R=(.*),G=(.*),B=(.*),A=(.*)\)')

    def __init__(self, color_str="(R=0,G=0,B=0,A=255)"):
        self.m_color_str = color_str
        match = self.regexp.match(color_str)
        (self.m_r, self.m_g, self.m_b, self.m_a) = [int(match.group(i)) for i in range(1, 5)]

    def __repr__(self):
        return self.m_color_str

    def parse_json(self, jsonColor):

        self.m_r = int(jsonColor["r"])
        self.m_g = int(jsonColor["g"])
        self.m_b = int(jsonColor["b"])

    def to_json(self):

        color_json_ = {}
        color_json_["r"] = str(self.m_r)
        color_json_["g"] = str(self.m_g)
        color_json_["b"] = str(self.m_b)
        return color_json_
