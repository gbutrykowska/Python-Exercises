# Napisz kolko i krzyzyk.

from enum import Enum # dla Python >3.6, dla wersji 2.7 from aenum import Enum

class GameState(Enum):
    IN_PROGRESS = 1
    OVER = 2


class FieldOption(Enum):
    O = 1
    X = 2
    EMPTY = 3


class Player(Enum):
    ONE = 1
    TWO = 2


class TicTacToe(object):
    def __init__(self):
        self.gameState = GameState.IN_PROGRESS
        self.board = [[FieldOption.EMPTY, FieldOption.EMPTY, FieldOption.EMPTY],
                      [FieldOption.EMPTY, FieldOption.EMPTY, FieldOption.EMPTY],
                      [FieldOption.EMPTY, FieldOption.EMPTY, FieldOption.EMPTY]]
        self.activePlayer = Player.ONE

    def checkGameState(self):
        if all(field == board[0,0] for field in board[0]):
            self.gameState = GameState.OVER
        elif all(field == board[1,0] for field in board[1]):
            self.gameState = GameState.OVER
        elif all(field == board[2,0] for field in board[2]):
            self.gameState = GameState.OVER
        elif board[0,0] == board[1,0] == board[2,0]:
            self.gameState = GameState.OVER
        elif board[0,1] == board[1,1] == board[2,1]:
            self.gameState = GameState.OVER
        elif board[0,2] == board[1,2] == board[2,2]:
            self.gameState = GameState.OVER
        elif board[2,0] == board[1,1] == board[0,2]:
            self.gameState = GameState.OVER
        else:
            self.gameState = GameState.IN_PROGRESS
        return self.gameState

    def isMoveValid(self, row, col):
        return self.board[row, col] == FieldOption.EMPTY

    def makeMove(self, row, col):
        if (self.activePlayer == Player.ONE):
            self.board[row, col] = FieldOption.O
        else:
            self.board[row, col] = FieldOption.X

    def switchPlayers(self):
        if (self.activePlayer == Player.ONE):
            self.activePlayer = Player.TWO
        else:
            self.activePlayer = Player.ONE

    def start(self):

        while self.gameState == GameState.IN_PROGRESS:
            print("Player: " + self.activePlayer.name + ": choose coordinate row: ")
            chosenRow = int(input())
            print("Player: " + self.activePlayer.name + ": choose coordinate col: ")
            chosenCol = int(input())

            if self.isMoveValid(chosenRow, chosenCol) :
                self.makeMove(chosenRow, chosenCol)
                self.switchPlayers()
                self.checkGameState()
            else:
                print("Move is not valid. Try again")

        if board.count(FieldOption.EMPTY) == 0 and self.gameState == GameState.IN_PROGRESS:
            print("Game over! It's a draw.")

        if self.gameState == GameState.OVER:
            if self.activePlayer == Player.ONE:
                print("Game over! Player One wins.")
            else:
                print("Game over! Player Two wins.")
            #tylko tu print i input



tictactoe = TicTacToe()
tictactoe.start()