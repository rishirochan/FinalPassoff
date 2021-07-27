# Tic Tac Toe
# We completely deleted the computer code, and added objects for players to make it easier
# We also have another class for the Board itself

import random

# This is the first class we have and it reliable for the Board and all the functions that relate to the Board
class TictactoeBoard:

    # This is the positioning of the board itself
    # It is the class property (dictionary)
    def __init__(self):
        self.board = {
            7: " ", 8: " ", 9: " ",
            4: " ", 5: " ", 6: " ",
            1: " ", 2: " ", 3: " "}

    # This is the class method that handles the placement of the board, like placing 'X' at position 8
    def drawBoard(self):
        # This is also the way the board will look
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    # This class method checks if the board is full or has any empty spaces
    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            # Another Class Method .isSpaceFree is in use to see if there are any empty spaces
            if self.isSpaceFree(i):
                return False
        return True

    # This class method takes the move that the player inputs and uses the .board property to place the letter
    def makeMove(self, letter, move):
        self.board[move] = letter

    # Checks if there are any empty spaces on the board
    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    # This class method runs through all the ways that one can win and if any are True, they win
    def isWinner(self, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == le and self.board[8] == le and self.board[9] == le) or # across the top
            (self.board[4] == le and self.board[5] == le and self.board[6] == le) or # across the middle
            (self.board[1] == le and self.board[2] == le and self.board[3] == le) or # across the bottom
            (self.board[7] == le and self.board[4] == le and self.board[1] == le) or # down the left side
            (self.board[8] == le and self.board[5] == le and self.board[2] == le) or # down the middle
            (self.board[9] == le and self.board[6] == le and self.board[3] == le) or # down the right side
            (self.board[7] == le and self.board[5] == le and self.board[3] == le) or # diagonal
            (self.board[9] == le and self.board[5] == le and self.board[1] == le)) # diagonal

# This is the second class, the player class, that is responsible for the Player's properties
class Player:

    # The 2 properties we have for the players are their names, and the letter they will use in the game
    def __init__(self, name):
        self.letter = ''
        self.name = name

    # This class method will use tttboard, which is just theBoard, and ask for the players move
    # while cross verifying if the space is empty
    def getPlayerMove(self,tttboard):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not tttboard.isSpaceFree(int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    # This class method takes player1's letter and assigns the other letter later on directly to player2
    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Hard graded in the while True, to give the other letter to player2
        while not (self.letter == 'X' or self.letter == 'O'):
            print('Do you, Player1, want to be X or O?')
            self.letter = input().upper()

    # Here Player 1 has a higher chance to go first but, Player2 also has a chance to go first
    def whoGoesFirst(self,player2):
        # Randomly choose the player who goes first, but with a higher chance to p1.
        if random.randint(0, 11) > 3:
            return self.name
        else:
            return player2.name

# This is the only function that is not in a class because it is just to play the game again.
def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

while True:
    print('Welcome to Tic Tac Toe!')
    # Here we create the objects, and in the player's we assign the name or a str value.
    theBoard=TictactoeBoard()
    player1=Player('player1')
    player2=Player('player2')

    # Player1 will give his letter
    player1.inputPlayerLetter()
    # Depending on p1s letter, the other letter is assigned to p2
    if player1.letter == 'X':
        player2.letter = 'O'
    else:
        player2.letter = 'X'

    # In order to use this function as a method in a class we took player1 as the object, and player2 into the parameter
    turn = player1.whoGoesFirst(player2)
    print(turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        # This checks whos turn it is and runs the code below
        if turn == 'player1':
            # Player's turn.
            # theBoard, the object, uses the class method .drawBoard to create the board.
            theBoard.drawBoard()
            # Player gives his move
            move = player1.getPlayerMove(theBoard)
            # the board implements the player's moves
            theBoard.makeMove(player1.letter, move)

            # Checks if the player has won
            # If they did, then game over p1 wins.
            if theBoard.isWinner(player1.letter):
                theBoard.drawBoard()
                print('Player1 has won the game! PLayer2 lost.')
                gameIsPlaying = False
            # Otherwise continue to next player's turn
            else:
                if theBoard.isBoardFull():
                    theBoard.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player2'

        else:
            # Player2's turn.
            # Same comments as above
            theBoard.drawBoard()
            move = player2.getPlayerMove(theBoard)
            theBoard.makeMove(player2.letter, move)

            if theBoard.isWinner(player2.letter):
                theBoard.drawBoard()
                print('Player2 has won the game! Player1 lose.')
                gameIsPlaying = False
            else:
                if theBoard.isBoardFull():
                    theBoard.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player1'
    # We utilize the only function and if True then the code will run all over again
    # Else it breaks from the while True loop
    if not playAgain():
        break