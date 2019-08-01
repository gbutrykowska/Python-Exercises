# Napisz kółko i krzyżyk.
class GameState(Enum):
    IN_PROGRESS = 1
    OVER = 2

class TicTacToe(object):
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    chosenField = 0
    def __init__(self, gameState, board, activePlayer = "playerOne"):
        self.gameState = gameState
        self.board = board
        self.activePlayer = activePlayer

    def gameStateChange(self, gameState):
        # if tree symbols in line
            # game over
                #O's - playerOne won
                #X's - playerTwo won
        # elif no empty fields, no symbols in line
            # game over - it's a draw
        # else
            # game in progress

    def move(self, chosenField):
        print("\n", board[0], "\n", board[1], "\n", board[2])
        chosenField = input("Please choose the field of your next move, by typing in the number: ")
        return chosenField

    def updateBoard(self, chosenfield, symbol):
        # if activePlayer == playerOne:
            #symbol = "O"
        # else:
            #symbol = "X"
        # if chosenField = 1:
            #board[0,0] = symbol itd.


    def game(self):

        while (gameState == GameState.IN_PROGRESS):
            #move
            #update board
            #check game status

            if (activePlayer == playerOne):
                activePlayer = playerTwo;
            else:
                activePlayer = playerOne





#____________________
play(): {

            // init()


która
"pobierze"
graczy
oraz
// zainicjalizuje
planszę \
// activePlayer = playerOne;

while (gameState == GameState.IN_PROGRESS) {

// pobierz ruch aktywnego gracza
// wykonaj ruch aktywnego gracza
// wyrysuj planszę
// sprawdz stan gry i przypisz do gameState
// podmien aktywnego gracza

// if (activePlayer == playerOne) activePlayer = playerTwo;
// else activePlayer = playerOne;
}