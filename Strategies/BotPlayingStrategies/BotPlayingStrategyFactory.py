from Game.BotDifficulty import BotDifficulty
from Strategies.BotPlayingStrategies.EasyBotPlayingStrategy import EasyBotPlayingStrategy
from Strategies.BotPlayingStrategies.MediumBotPlayingStrategy import MediumBotPlayingStrategy
from Strategies.BotPlayingStrategies.HardBotPlayingStrategy import HardBotPlayingStrategy
class BotPlayingStrategyFactory:
    def getBotPlayingStrategyForDifficultyLevel(botDifficultyLevel):
        if(botDifficultyLevel == BotDifficulty.EASY):
            return EasyBotPlayingStrategy()
        if(botDifficultyLevel == BotDifficulty.MEDIUM):
            return MediumBotPlayingStrategy()
        if(botDifficultyLevel == BotDifficulty.HARD):
            return HardBotPlayingStrategy()
        
        