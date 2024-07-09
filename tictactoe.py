"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # TODO: refactor this to be more efficient
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
            
    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    actions = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)
    
    new_board[action[0]][action[1]] = player(board)
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # TODO: refactor this to be more efficient
    response = None
    for row in board:
        if row[0] == row[1] == row[2]:
            response = row[0]
            break
    if response == None:
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i]:
                response = board[0][i]
                break
    if response == None:
        if board[0][0] == board[1][1] == board[2][2]:
            response = board[0][0]
        elif board[0][2] == board[1][1] == board[2][0]:
            response = board[0][2]
    if response == X:
        return 1
    elif response == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    raise NotImplementedError
