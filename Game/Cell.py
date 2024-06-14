from Game.CellState import CellState
class Cell:
    def __init__(self,row,col):
        self.__row = row
        self.__col = col
        self.__cellState = CellState.EMPTY
        self.__player = None

    def getrow(self):
        return self.__row

    def setrow(self, value):
        self.__row = value

    def getcol(self):
        return self.__col

    def setcol(self, value):
        self.__col = value

    def getcellState(self):
        return self.__cellState

    def setcellState(self, value):
        self.__cellState = value

    def getplayer(self):
        return self.__player

    def setplayer(self, value):
        self.__player = value
