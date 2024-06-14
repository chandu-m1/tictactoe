from Game.Game import Game
class GameController:
    def createGame(self,dimensions,players,winningstrategies):
        return Game().getbuilder().setdimensions(dimensions).setplayers(players).setwinningstrategies(winningstrategies).build()

    def displayBoard(self,game):
        game.printBoard()

    def undo(self,game):
        pass

    def makeMove(self,game):
        game.makemove()

    def getGameStatus(self,game):
        return game.getgamestatus()

    def printResult(self,game):
        game.printresult()

