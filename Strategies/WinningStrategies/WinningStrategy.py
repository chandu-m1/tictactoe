from abc import ABC, abstractmethod

class Winningstrategy(ABC):
    @abstractmethod
    def checWinner(self,board,move):
        pass