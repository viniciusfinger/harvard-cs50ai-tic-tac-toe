"""
Tic Tac Toe Player
"""

from copy import deepcopy


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
    if utility(board) == 1:
        print("X wins")
        return X
    elif utility(board) == -1:
        print("O wins")
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if utility(board) != 0:
        return True
    
    for row in board:
        if None in row:
            return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    # Check row win
    for row in board:
        if row[0] == row[1] == row[2] and not row[1] == None:
            if row[0] == X:
                return 1
            else:
                return -1
    
    # Check column win
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and not board[1][i] == None:
            if board[0][i] == X:
                return 1
            else:
                return -1
    
    # Check diagonal win from top left to bottom right
    if board[0][0] == board[1][1] == board[2][2] and not board[1][1] == None:
        if board[0][0] == X:
            return 1
        else:
            return -1
        
    # Check diagonal win from top right to bottom left
    if board[0][2] == board[1][1] == board[2][0] and not board[1][1] == None:
        if board[0][2] == X:
            return 1
        else:
            return -1
    
    return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Implement the minimax algorithm
    if terminal(board):
        return None
    
    if player(board) == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]
    
def max_value(board):
    if terminal(board):
        return utility(board), None
    
    v = float('-inf')
    best_action = None
    for action in actions(board):
        min_val = min_value(result(board, action))[0]
        if min_val > v:
            v = min_val
            best_action = action
            
    return v, best_action

def min_value(board):
    if terminal(board):
        return utility(board), None
    
    v = float('inf')
    best_action = None
    for action in actions(board):
        max_val = max_value(result(board, action))[0]
        if max_val < v:
            v = max_val
            best_action = action
            
    return v, best_action

