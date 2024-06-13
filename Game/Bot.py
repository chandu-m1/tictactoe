from Player import Player
from PlayerType import PlayerType
class Bot(Player):
    def __init__(self, symbol, name, botDifficultyLevel):
        super().__init__(symbol, name, PlayerType.BOT)
        self.__botDifficultyLevel = botDifficultyLevel