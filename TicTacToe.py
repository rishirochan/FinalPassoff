# Tic Tac Toe
import random

class TictactoeBoard:
    def __init__(self):
        self.board = {
            7: " ", 8: " ", 9: " ",
            4: " ", 5: " ", 6: " ",
            1: " ", 2: " ", 3: " "}

    def drawBoard(self):
        # This function prints out the board that it was passed.
        # "board" is a list of 10 strings representing the board (ignore index 0)
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

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True

    def makeMove(self, letter, move):
        self.board[move] = letter

    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

class Player:
    def __init__(self, name):
        self.letter = ''
        self.name = name

    def getPlayerMove(self,tttboard):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not tttboard.isSpaceFree(int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        while not (self.letter == 'X' or self.letter == 'O'):
            print('Do you, Player1, want to be X or O?')
            self.letter = input().upper()

def whoGoesFirst(player1,player2) -> object:
    # Randomly choose the player who goes first.
    if random.randint(0, 11) > 3:
        return player1
    else:
        return player2

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo.board[7] == le and bo.board[8] == le and bo.board[9] == le) or # across the top
            (bo.board[4] == le and bo.board[5] == le and bo.board[6] == le) or # across the middle
            (bo.board[1] == le and bo.board[2] == le and bo.board[3] == le) or # across the bottom
            (bo.board[7] == le and bo.board[4] == le and bo.board[1] == le) or # down the left side
            (bo.board[8] == le and bo.board[5] == le and bo.board[2] == le) or # down the middle
            (bo.board[9] == le and bo.board[6] == le and bo.board[3] == le) or # down the right side
            (bo.board[7] == le and bo.board[5] == le and bo.board[3] == le) or # diagonal
            (bo.board[9] == le and bo.board[5] == le and bo.board[1] == le)) # diagonal

while True:
    print('Welcome to Tic Tac Toe!')
    theBoard=TictactoeBoard()
    player1=Player('player1')
    player2=Player('player2')

    player1.inputPlayerLetter()
    if player1.letter == 'X':
        player2.letter = 'O'
    else:
        player2.letter = 'X'
    turn = whoGoesFirst(player1, player2)
    print(turn.name + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn.name == 'player1':
            # Player's turn.
            theBoard.drawBoard()
            move = player1.getPlayerMove(theBoard)
            theBoard.makeMove(player1.letter, move)

            if isWinner(theBoard, player1.letter):
                theBoard.drawBoard()
                print('Player1 has won the game! PLayer2 lost.')
                gameIsPlaying = False
            else:
                if theBoard.isBoardFull():
                    theBoard.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = player2

        else:
            # Computer's turn.
            theBoard.drawBoard()
            move = player2.getPlayerMove(theBoard)
            theBoard.makeMove(player2.letter, move)

            if isWinner(theBoard, player2.letter):
                theBoard.drawBoard()
                print('Player2 has won the game! Player1 lose.')
                gameIsPlaying = False
            else:
                if theBoard.isBoardFull():
                    theBoard.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = player1

    if not playAgain():
        break