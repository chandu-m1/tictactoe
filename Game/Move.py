class Move:
    def __init__(self,player,cell):
        self.__player = player
        self.__cell = cell

    def getplayer(self):
        return self.__player
    def setplayer(self,value):
        self.__player = value
    def getcell(self):
        return self.__cell
    def setcell(self,value):
        self.__cell = value