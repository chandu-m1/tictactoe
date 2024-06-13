from abc import ABC, abstractmethod

class BotPlayingStrategy(ABC):
    @abstractmethod
    def makeMove(board):
        pass    