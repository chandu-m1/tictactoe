from Game.Player import Player
from Game.PlayerType import PlayerType
class Bot(Player):
    def __init__(self, symbol, name, botDifficultyLevel):
        super().__init__(symbol, name, PlayerType.BOT)
        self.__botDifficultyLevel = botDifficultyLevel

    def getbotdifficultylevel(self):
        return self.__botDifficultyLevel

    def getbotdifficultylevel(self,value):
        self.__botDifficultyLevel = value

    def makemove(self):
        pass