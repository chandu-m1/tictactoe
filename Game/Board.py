from Game.Cell import Cell
from Game.CellState import CellState
class Board:
    def __init__(self, size):
        self.__dim = size
        self.__board = [[Cell(i,j) for j in range(0,size)] for i in range(0, size)]

   
    def getdim(self):
        return self.__dim

    def getdim(self, value):
        self.__dim = value

    def getboard(self):
        return self.__board

    def setboard(self, value):
        self.__board = value


    def print(self):
        for i in range(0,self.dim):
            print("|")
            for j in range(0,self.dim):
                cell = self.__board[i][j]
                if(cell.getcellState == CellState.EMPTY):
                    print(" - |", sep="")
                else:
                    print(" "+cell.getplayer().getsymbol().getachar()+" |",sep="")
            print()
        