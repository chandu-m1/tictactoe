from abc import ABC, abstractmethod

class Winningstrategy(ABC):
    @abstractmethod
    def checkWinner(self,board,move):
        pass