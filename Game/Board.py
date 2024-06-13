from Cell import Cell
class Board:
    def __init__(self, size):
        self.__dim = size
        self.__board = [[Cell(i,j) for j in range(0,size)] for i in range(0, size)]

    @property
    def _dim(self):
        return self.__dim

    @_dim.setter
    def _dim(self, value):
        self.__dim = value

    @property
    def _board(self):
        return self.__board

    @_board.setter
    def _board(self, value):
        self.__board = value


    def displayBoard(self):
        for i in range(0,self.dim):
            for j in range(0,self.dim):
                print(self.__board[i][j])
        