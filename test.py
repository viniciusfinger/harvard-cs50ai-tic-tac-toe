from tictactoe import *

board = [[X, EMPTY, O],
        [X, O, EMPTY],
        [EMPTY, EMPTY, EMPTY]]

action = list(actions(board))[0]

result(board, action)