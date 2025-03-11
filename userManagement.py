import psycopg2

from player import Player
from game import Game
from gameTypes import GameType
import json
import os

user_players = {}

player_cockfights = {}

player_specialcock = {}

DATABASE_URL = os.getenv("DATABASE_URL")
connection = psycopg2.connect(DATABASE_URL)

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
    global player_cockfights
    if messageID in player_cockfights:
        del player_cockfights[messageID]

def remove_specialcock(messageID):
    global player_specialcock
    if messageID in player_specialcock:
        del player_specialcock[messageID]

def get_cockfight(messageID):
    if messageID not in player_cockfights:
        return None
    return player_cockfights[messageID]

def get_specialcock(messageID):
    if messageID not in player_specialcock:
        return None
    return player_specialcock[messageID]


def getAllUsers():
    users = {
        "@ooo155",
        "@EinKlassiker",
        "@CE0Flex",
        "@schuizreal",
        "@Rudi121333",
        "@Martin1509"
    }
    return users

def save_players():
    for player in user_players.values():
        player.save_to_db(connection)

def load_players():
    try:
        with open(PLAYER_SAVE_FILE_NAME, "r") as file:
            user_players = [Player.from_dict(player_data) for player_data in json.load(file)]
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return empty list if file doesn't exist or is empty

