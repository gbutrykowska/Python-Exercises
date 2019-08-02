# Napisz kółko i krzyżyk.

from enum import Enum
class GameState(Enum):
    IN_PROGRESS = 1
    OVER = 2
class fieldOptions(Enum):
    O = 1
    X = 2
    EMPTY = 3

class TicTacToe(object):

    board = [[fieldOptions.EMPTY, fieldOptions.EMPTY. fieldOptions.EMPTY],
             [fieldOptions.EMPTY, fieldOptions.EMPTY, fieldOptions.EMPTY],
             [fieldOptions.EMPTY, fieldOptions.EMPTY, fieldOptions.EMPTY]]
    chosenField = 0
    gameState = GameState.IN_PROGRESS

    def __init__(self, gameState, board, activePlayer = "playerOne"):
        self.gameState = gameState
        self.board = board
        self.activePlayer = activePlayer

    def symbolsInLine(self, symbol, threeInLine):
        self.symbol = symbol #tu coś namieszałam, muszę poprawić
        self.threeInLine = False
        for field in board:
            if field board[0,0] and [0,1] and [0,2] == symbol:
                threeInLine = True
            elif field board[1,0] and [1,1] and [1,2] == symbol:
                threeInLine = True
            elif field board[2,0] and [2,1] and [2,2] == symbol:
                threeInLine = True
            elif field board[0,0] and [1,0] and [2,0] == symbol:
                threeInLine = True
            elif field board[0,1] and [1,1] and [2,1] == symbol:
                threeInLine = True
            elif field board[0,2] and [1,2] and [2,2] == symbol:
                threeInLine = True
            elif field board[0,0] and [1,1] and [2,2] == symbol:
                threeInLine = True
            elif field board[2,0] and [1,1] and [0,2] == symbol:
                threeInLine = True
            #To powinnam napisać jakoś ładniej
        return threeInLine

    def gameStateChange(self, gameState):
        if threeInLine == True:
            gameState = GameState.OVER
            if symbolsInLine.symbol == fieldOptions.O:
                print("Game over! Player One won the game.")
            if symbolsInLine.symbol == fieldOptions.X:
                print("Game over! Player Two won the game.")
        elif board.count(fieldOptions.EMPTY) == 0:
            gameState = GameState.OVER
            print("Game over! It's a draw.")
        else:
            gameState = GameState.IN_PROGRESS
        return gameState

    def move(self, numBoard, chosenField):
        self.numBoard = [["1", "2", "3"],
                 ["4", "5", "6"],
                 ["7", "8", "9"]]
        print("\n", numBoard[0], "\n", numBoard[1], "\n", numBoard[2])
        self.chosenField = input("Please choose the field of your next move, by typing in the number: ")
        return chosenField

    def updateBoard(self, chosenField, symbol):
        if activePlayer == playerOne:
            self.symbol = fieldOptions.O
        else:
            self.symbol = fieldOptions.X
        if chosenField == 1:
            board[0,0] = symbol
        elif chosenField == 2:
            board[0,1] = symbol
        elif chosenField == 3:
            board[0,2] = symbol
        elif chosenField == 4:
            board[1,0] = symbol
        elif chosenField == 5:
            board[1,1] = symbol
        elif chosenField == 6:
            board[1,2] = symbol
        elif chosenField == 7:
            board[2,0] = symbol
        elif chosenField == 8:
            board[2,1] = symbol
        elif chosenField == 9:
            board[2,2] = symbol
        else:
            print("Wrong field number")
        return board
        #To też na pewno mogę napisać jakoś ładniej
        #Dodać opcję akcji jeśli pole nie jest puste

    def game(self):

        while (gameState == GameState.IN_PROGRESS):
            #move
            #update board
            #check game status

            if (activePlayer == playerOne):
                activePlayer = playerTwo;
            else:
                activePlayer = playerOne

#sprawdzić czy wszystkie metody mają swoje parametry