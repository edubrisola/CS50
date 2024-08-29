"""
Tic Tac Toe Player
"""

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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    coordinates = set()
    for rows in range(3):
        for char in range(3):
            if board[rows][char] == EMPTY:
                coordinate = (rows, char)
                coordinates.add(coordinate)

    return coordinates


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not (0 <= action[0] < len(board) and 0 <= action[1] < len(board[0])):
        raise Exception("Move out of bounds")
    if board[action[0]][action[1]] is not None:
        raise Exception("Cell already taken")

    new_board = [row.copy() for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for rows in board:
        if X == rows[0] and X == rows[1] and X == rows[2]:
            return X
        elif O == rows[0] and O == rows[1] and O == rows[2]:
            return O

    for collumn in range(3):
        if X == board[0][collumn] and X == board[1][collumn] and X == board[2][collumn]:
            return X
        elif O == board[0][collumn] and O == board[1][collumn] and O == board[2][collumn]:
            return O

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    elif win != X and win != O:
        return 0


def minimax(board):
    if terminal(board):
        return None
    if player(board) == "X":
        return max_value(board)[0]
    else:
        return min_value(board)[0]

def max_value(board):
    if terminal(board):
        return None, utility(board)

    v = float("-inf")
    best_move = None

    for action in actions(board):
        _, min_v = min_value(result(board, action))
        if min_v > v:
            v = min_v
            best_move = action

    return best_move, v

def min_value(board):
    if terminal(board):
        return None, utility(board)

    v = float("inf")
    best_move = None

    for action in actions(board):
        _, max_v = max_value(result(board, action))
        if max_v < v:
            v = max_v
            best_move = action

    return best_move, v
