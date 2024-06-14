from Game.Player import Player
from Game.PlayerType import PlayerType
from Strategies.BotPlayingStrategies.BotPlayingStrategyFactory import BotPlayingStrategyFactory
class Bot(Player):
    def __init__(self, symbol, name, botDifficultyLevel):
        super().__init__(symbol, name, PlayerType.BOT)
        self.__botDifficultyLevel = botDifficultyLevel
        print(self.__botDifficultyLevel)
        self.__botPlayingStrategy = BotPlayingStrategyFactory.getBotPlayingStrategyForDifficultyLevel(botDifficultyLevel)

    def getbotdifficultylevel(self):
        return self.__botDifficultyLevel

    def getbotdifficultylevel(self,value):
        self.__botDifficultyLevel = value

    def makemove(self,board):
        print(self.__botPlayingStrategy)
        return self.__botPlayingStrategy.makeMove(board)