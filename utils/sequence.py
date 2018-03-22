import json

class Sequence:

    def __init__(self):

        self.m_name = None
        self.m_frames = []
        self.m_total_frames = 0

    def __repr__(self):

        return "Sequence(name: {0}, total_frames: {1})".format(
                self.m_name,
                self.m_total_frames)

    def load(self, sequenceFile):
        with open(sequenceFile) as f:
            sequence_json = json.load(f)

            self.m_name = sequence_json["name"]
            self.m_frames = sequence_json["frames"]
            self.m_total_frames = sequence_json["total_frames"]

    def save(self, sequenceFile):
        sequence_ = {}
        sequence_["name"] = self.m_name
        sequence_["total_frames"] = self.m_total_frames
        sequence_["frames"] = self.m_frames

        with open(sequenceFile, 'w') as f:
            f.write(json.dumps(sequence_, indent=2))
