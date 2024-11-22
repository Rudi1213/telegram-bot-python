import random

def cockfight(player1, player2):
    winner = random.randint(1,2)
    if winner == 1:
        player1.score = player1.score+5
        player2.score = player2.score-2
        return player1
    else:
        player2.score = player2.score+5
        player1.score = player1.score-2
        return player2


def multiplyCock(player,multiplicator):
    player.score = player.score*multiplicator

def divideCock(player,divisor):
    player.score = player.score/divisor

def growCock(player,amount):
    player.score = player.score+amount

def shrinkCock(player,amount):
    player.score = player.score-amount