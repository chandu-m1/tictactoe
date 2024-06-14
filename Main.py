from GameController.GameController import GameController
from Game.GameStatus import GameStatus
from Game.Player import Player
from Game.Bot import Bot
from Game.Symbol import Symbol
from Game.PlayerType import PlayerType
from Game.BotDifficulty import BotDifficulty
from Strategies.WinningStrategies.RowWinningStrategy import RowWinningStategy
from Strategies.WinningStrategies.ColumnWinningStrategy import ColumnWinningStrategy
from Strategies.WinningStrategies.DiagonalWinningStrategy import DiagonalWinningStrategy
class Main:
    def main(self):
        #create a game
        gameController = GameController()
        try:
            game = gameController.createGame(3,[Player(Symbol("x"),"Chandu",PlayerType.HUMAN), Bot(Symbol("O"),"Rahul",BotDifficulty.EASY)],[RowWinningStategy(), ColumnWinningStrategy(),DiagonalWinningStrategy()])
        except:
            print("Something went wrong")
            game.setgameStatus(GameStatus.ENDED)

        print("-------------------Game is starting-------------------")
        # while game status is in progress
        while(gameController.getGameStatus(game) == GameStatus.IN_Progress):
            #print board
            print("This is how boards looks like : ")   
            gameController.displayBoard(game)
            #print if undo
            print("Do you want to undo? (y/n)")
            #if yes call undo
            inp = input()
            if(inp == "yes" or inp == "YES"):
                gameController.undo(game)
            else:
                gameController.makeMove(game)
    
        #check game status
        gameController.printResult(game)


if __name__ == "__main__":
    main = Main()
    main.main()

