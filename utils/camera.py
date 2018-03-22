import json

class Camera:

    def __init__(self):
        self.cx = 320.0
        self.cy = 240.0
        self.fx = 320.0
        self.fy = 320.0
        self.fov = 90
        self.depthmin = 0.0
        self.depthmax = 7.0

    def __repr__(self):
        return "Camera(cx: {0}, cy: {1}, fx: {2}, fy: {3}, fov: {4}, depthmin: {5}, depthmax: {6})".format(
                self.cx,
                self.cy,
                self.fx,
                self.fy,
                self.fov,
                self.depthmin,
                self.depthmax)

    def load(self, cameraFile):
        with open(cameraFile) as f:
            camera_json = json.load(f)

            self.cx = camera_json["cx"]
            self.cy = camera_json["cy"]
            self.fx = camera_json["fx"]
            self.fy = camera_json["fy"]
            self.fov = camera_json["fov"]
            self.depthmin = camera_json["depthmin"]
            self.depthmax = camera_json["depthmax"]

    def save(self, cameraFile):
        camera = {}
        camera["cx"] = self.cx
        camera["cy"] = self.cy
        camera["fx"] = self.fx
        camera["fy"] = self.fy
        camera["fov"] = self.fov
        camera["depthmin"] = self.depthmin
        camera["depthmax"] = self.depthmax

        with open(cameraFile, 'w') as f:
            json.dump(camera, f, indent=2)
