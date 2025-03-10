import json

class Player:

    def __init__(self, user_id, name):
        self.score = 10
        self.user_id = user_id
        self.name = name

    def to_dict(self):
        return {"user_id": self.user_id, "name": self.name, "score": self.score}

    @classmethod
    def from_dict(cls, data):
        player = cls(data["user_id"], data["name"])
        player.score = data["score"]
        return player