class Player:
    def __init__(self,symbol,name,playerType):
        self.__symbol = symbol
        self.__name = name 
        self.__playerType = playerType

    def getsymbol(self):
         return self.__symbol
    def setsymbol(self,value):
        self.__symbol = value
    def getname(self):
        return self.__name
    def setname(self,value):
        self.__name = value

    def getplayertype(self):
        return self.__playerType
    def setplayertype(self,value):
        self.__playerType = value


    def makemove(self):
        pass