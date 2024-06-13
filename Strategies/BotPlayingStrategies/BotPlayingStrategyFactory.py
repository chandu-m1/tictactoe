from Game.BotDifficulty import BotDifficulty
from EasyBotPlayingStrategy import EasyBotPlayingStrategy
from MediumBotPlayingStrategy import MediumBotPlayingStrategy
from HardBotPlayingStrategy import HardBotPlayingStrategy
class BotPlayingStrategyFactory:
    def getBotPlayingStrategyForDifficultyLevel(botDifficultyLevel):
        if(botDifficultyLevel == BotDifficulty.EASY):
            return EasyBotPlayingStrategy()
        if(botDifficultyLevel == BotDifficulty.MEDIUM):
            return MediumBotPlayingStrategy()
        if(botDifficultyLevel == BotDifficulty.HARD):
            return HardBotPlayingStrategy()
        
        