from CellState import CellState
class Cell:
    def __init__(self,row,col):
        self.__row = row
        self.__col = col
        self.__cellState = CellState.EMPTY
        self.__player = None

    @property
    def _row(self):
        return self.__row

    @_row.setter
    def _row(self, value):
        self.__row = value

    @property
    def _col(self):
        return self.__col

    @_col.setter
    def _col(self, value):
        self.__col = value

    @property
    def _cellState(self):
        return self.__cellState

    @_cellState.setter
    def _cellState(self, value):
        self.__cellState = value

    @property
    def _player(self):
        return self.__player

    @_player.setter
    def _player(self, value):
        self.__player = value
