from player import Player
from game import Game
from gameTypes import GameType

user_players = {}

player_cockfights = {}

player_specialcock = {}


def add_player(user_id, name):
    if user_id not in user_players:
        user_players[user_id] = Player(user_id, name)


def get_player(user_id):
    if user_id not in user_players:
        return None
    return user_players[user_id]

def getAllPlayerScores():
    nameScores = {}
    for user_id, player in user_players.items():
        nameScores[player.name] = player.score

    return nameScores

def add_cockfight(player,messageID):
    player_cockfights[messageID] = Game(player, messageID, GameType.COCKFIGHT)

def add_specialcock(player,messageID):
    player_specialcock[messageID] = Game(player, messageID, GameType.SPECIAL)

def remove_cockfight(messageID):
    player_cockfights[messageID].delete()

def remove_specialcock(messageID):
    player_specialcock[messageID].delete()

def get_cockfight(messageID):
    if messageID not in player_cockfights:
        return None
    return player_cockfights[messageID]

def get_specialcock(messageID):
    if messageID not in player_specialcock:
        return None
    return player_specialcock[messageID]
