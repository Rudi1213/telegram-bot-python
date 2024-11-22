from gameTypes import GameType


class Game:
    def __init__(self, player, messageID, gameType):
        self.player = player
        self.messageID = messageID
        self.gameType = gameType
        if gameType == GameType.SPECIAL:
            self.guesses = 2

