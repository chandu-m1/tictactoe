from Board import Board
import Player
from GameStatus import GameStatus
class Game:
    def __init__(self,dimensions,players,winningStrategies):
        self.__moves = []
        self.__board = Board(dimensions)
        self.__players = players
        self.__currentPlayer = 0
        self.__winningStrategies = winningStrategies
        self.__gameStatus = GameStatus.IN_Progress
        self.__winner = None

    @property
    def _moves(self):
        return self.__moves

    @_moves.setter
    def _moves(self, value):
        self.__moves = value

    @property
    def _board(self):
        return self.__board

    @_board.setter
    def _board(self, value):
        self.__board = value

    @property
    def _players(self):
        return self.__players

    @_players.setter
    def _players(self, value):
        self.__players = value

    @property
    def _currentPlayer(self):
        return self.__currentPlayer

    @_currentPlayer.setter
    def _currentPlayer(self, value):
        self.__currentPlayer = value

    @property
    def _winningStrategies(self):
        return self.__winningStrategies

    @_winningStrategies.setter
    def _winningStrategies(self, value):
        self.__winningStrategies = value

    @property
    def _gameStatus(self):
        return self.__gameStatus

    @_gameStatus.setter
    def _gameStatus(self, value):
        self.__gameStatus = value

    @property
    def _winner(self):
        return self.__winner

    @_winner.setter
    def _winner(self, value):
        self.__winner = value

        
        
