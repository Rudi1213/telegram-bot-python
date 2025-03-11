import json
import os
import psycopg2

class Player:

    def __init__(self, user_id, name):
        self.score = 10
        self.user_id = user_id
        self.name = name

    def save_to_db(self, connection):
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO players (id, name, score)VALUES (%s, %s, %s)""", (self.user_id, self.name, self.score))
            connection.commit()








    def to_dict(self):
        return {"user_id": self.user_id, "name": self.name, "score": self.score}

    @classmethod
    def from_dict(cls, data):
        player = cls(data["user_id"], data["name"])
        player.score = data["score"]
        return player