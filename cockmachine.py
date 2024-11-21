import random

def cockfight(player1, player2):
    winner = random.randint(1,2)
    if winner == 1:
        player1.score = player1.score+10
        player2.score = player2.score-1
        return player1
    else:
        player2.score = player2.score+10
        player1.score = player1.score-1
        return player2


