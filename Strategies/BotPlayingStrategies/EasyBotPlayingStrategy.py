from Strategies.BotPlayingStrategies.BotPlayingStrategy import BotPlayingStrategy
from Game.CellState import CellState
class EasyBotPlayingStrategy(BotPlayingStrategy):
    def makeMove(self,board):
        dim = board.getdim()
        for i in range(0,dim):
            for j in range(0,dim):
                if(board.getboard()[i][j].getcellState() == CellState.EMPTY):
                    return board.getboard()[i][j]