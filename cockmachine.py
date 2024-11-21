from random import random
from player import Player

def cockfight(player1, player2):
    winner = random.randint(1,2)
    if winner == 1:
        player1.score = player1.score+1
        player2.score = player2.score-1
    else:
        player2.score = player2.score+1
        player1.score = player1.score-1


