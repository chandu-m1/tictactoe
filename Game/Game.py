from Game.Board import Board
from Game.PlayerType import PlayerType
from Game.GameStatus import GameStatus
from Game.CellState import CellState
from Game.Move import Move
class Game:
    def __init__(self,dimensions,players,winningStrategies):
        self.__moves = []
        self.__board = Board(dimensions)
        self.__players = players
        self.__currentPlayer = 0
        self.__winningStrategies = winningStrategies
        self.__gameStatus = GameStatus.IN_Progress
        self.__winner = None

    def getmoves(self):
        return self.__moves

    def setmoves(self, value):
        self.__moves = value

    def getboard(self):
        return self.__board

    def setboard(self, value):
        self.__board = value

    def getplayers(self):
        return self.__players

    def setplayers(self, value):
        self.__players = value

    def getcurrentPlayer(self):
        return self.__currentPlayer

    def setcurrentPlayer(self, value):
        self.__currentPlayer = value

    def getwinningStrategies(self):
        return self.__winningStrategies

    def setwinningStrategies(self, value):
        self.__winningStrategies = value

    
    def getgameStatus(self):
        return self.__gameStatus

    def setgameStatus(self, value):
        self.__gameStatus = value

    def getwinner(self):
        return self.__winner

    def setwinner(self, value):
        self.__winner = value

    def validatemove(self,cell):
        row = cell.getrow()
        col = cell.getcol()
        if(row<0 or col<0 or row>=self.__board.getdim() or col >= self.__board.getdim()):
            return False
        if(self.__board.getboard()[row][col].getcellstate() == CellState.EMPTY):
            return True
        return False

    def makemove(self):
        currentPlayer = self.__players[self.__currentPlayer]
        proposedcell = currentPlayer.makemove()
        if(not self.validatemove(proposedcell)):
            return
        cellinboard = self.__board.getboard()[proposedcell.getrow()][proposedcell.getcol()]
        cellinboard.setcellstate(CellState.FILLED)
        cellinboard.setplayer(currentPlayer)

        move = Move(currentPlayer, cellinboard)
        self.__moves.append(move)
        for winninstrategy in self.__winningStrategies:
            if(winninstrategy.checkwinner(self.__board,move)):
                self.__gameStatus = GameStatus.ENDED
                self.__winner = currentPlayer
                return
        if(len(self.__moves) == self.__board.getdim()* self.__board.getdim()):
            self.__gameStatus = GameStatus.DRAW
            return
        self.__currentPlayer += 1
        self.__currentPlayer %= len(self.__players) 
    
    

    def printBoard(self):
        self.__board.print()
    def getbuilder(self):
        return self.Builder()

    def printresult(self):
        if(self.__gameStatus == GameStatus.ENDED):
            print("Game has ended")
            print("Winner is : "+self.__winner.getname())
        else:
            print("Game is draw")

    class Builder:
        def setdimensions(self,value):
            self.__dimesion = value
            return self
        def setplayers(self,value):
            self.__players = value
            return self
        def setwinningstrategies(self,value):
            self.__winningstrategies = value
            return self
        
        def valid(self):
            if(len(self.__players)<2):
                return False
            if(len(self.__players)!= self.__dimesion):
                return False
            botCount = 0
            for player in self.__players:
                if(player.getplayertype() == PlayerType.BOT):
                    botCount +=1
            
            if(botCount>=2):
                return False
            
            symbols= set()
            for player in self.__players:
                if player.getsymbol.getachar() in symbols:
                    return False
                symbols.add(player.getsymbol.getachar())
            return True


        def build(self):
            if(not self.valid()):
                raise RuntimeError("Not valid")
            print(self.__dimesion, self.__players,self.__winningstrategies)
            return Game(self.__dimesion, self.__players,self.__winningstrategies)
        



        
        
