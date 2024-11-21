from player import Player

user_players = {}

def add_player(user_id, name):
    if user_id not in user_players:
        user_players[user_id] = Player(user_id, name)


def get_player(user_id):
    if user_id not in user_players:
        return None
    return user_players[user_id]

