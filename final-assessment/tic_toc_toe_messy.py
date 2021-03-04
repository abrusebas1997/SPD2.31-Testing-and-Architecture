# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html.

# TODOs:
# 1. Find all TODO items and see whether you can improve the code.
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings (use """ insted of # for function's header
#    comments)

import random

# "board" is a list of 10 strings representing the board (ignore index 0)
BOARD_SIZE = 10

def drawBoard(board):
    """ This function prints out the board that it was passed. """

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |\n')

def inputPlayerLetter():
    """
    Lets the player type which letter they want to be.
    Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    """
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    """ Randomly choose the player who goes first. """
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    """ This function returns True if the player wants to play again, otherwise it returns False. """
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    """
    Given a board and a player’s letter, this function returns True if that player has won.
    We use bo instead of board and le instead of letter so we don’t have to type as much.
    """
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    """Make a duplicate of the board list and return it the duplicate."""
    return board.copy()

def isSpaceFree(board, move):
    """Return true if the passed move is free on the passed board."""
    return board[move] == ' '

def getPlayerMove(board):
    """Let the player type in their move."""

    playerInput = ' ' # W0621: Redefining name 'move' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    while playerInput not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(playerInput)):
        print('What is your next move? (1-9)')
        playerInput = input()
    return int(playerInput)

def chooseRandomMoveFromList(board, movesList):
    """Returns a valid move from the passed list on the passed board.
    Returns None if there is no valid move."""
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if possibleMoves:
        return random.choice(possibleMoves)
    return None

def getComputerMove(board, letters):
    """
    Given a board and the computer's letter, determine where to move and return that move.

    Here is our algorithm for our Tic Tac Toe AI:
      First, check if we can win in the next move
      Check if the player could win on their next move, and block them.
      Try to take one of the corners, if they are free.
      Try to take the center, if it is free.
      Move on one of the sides.

     inputPlayerLetter() returns Player and computer letters in list at index 0 and 1 respectively
    """
    player = letters[0]
    computer = letters[1]

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1,BOARD_SIZE):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computer, i)
            if isWinner(copy, computer):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1,BOARD_SIZE):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, player, i)
            if isWinner(copy, player):
                return i

    # Try to take one of the corners, if they are free.
    preferredMove = chooseRandomMoveFromList(board, [1, 3, 7, 9])

    # Hint: Comparisons to singletons like None should always be done with is or is not, never the equality/inequality operators.)
    if preferredMove is not None:
        return preferredMove

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    """Return True if every space on the board has been taken. Otherwise return False."""
    for i in range(1,BOARD_SIZE):
        if isSpaceFree(board, i):
            return False
    return True

def initGamePrompt():
    ''' Initialize Game Prompt'''
    print('Welcome to Tic Tac Toe!')

    while True:

        assignedLetters = inputPlayerLetter()

        firstTurn = whoGoesFirst()
        print('The ' + firstTurn + ' will go first.')

        startGame(firstTurn, assignedLetters)

        if not playAgain():
            break

def startGame(firstMove, letters):
    ''' Start the game. The

    Arguments:
    firstMove -> str: whoever gets returned by whoGoesFirst()
    letters -> list: 'x' or 'o' assignments for player & computer at index 0,1 respectively

    '''

    # Reset the board
    theBoard = [' '] * BOARD_SIZE
    # drawBoard(theBoard)

    if firstMove == 'player':
        currentMove = 0
    else:
        # computer goes first
        currentMove = 1

    while True:
        # Player’s turn.
        if currentMove == 0:
            move = getPlayerMove(theBoard)
        else:
            print("Computer's Turn")
            move = getComputerMove(theBoard, letters)

        # Make the move and update board
        makeMove(theBoard, letters[currentMove], move)
        drawBoard(theBoard)

        if isWinner(theBoard, letters[currentMove]):
            if currentMove == 0:
                print('Hooray! You have won the game!')
            else:
                print('The computer has beaten you! You lose.')
            break

        if isBoardFull(theBoard):
            print('The game is a tie!')
            break

        # Toggles current move between player and computer
        currentMove ^= 1

if __name__ == "__main__":
    initGamePrompt()
