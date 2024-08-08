"""
Tic Tac Toe Player
"""

import math
import copy

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

    Args:
        board (list): The current state of the board.

    Returns:
        str: The player who has the next turn (X or O).
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.

    Args:
        board (list): The current state of the board.

    Returns:
        set: A set of tuples representing all possible actions.
    """
    possible_actions = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                possible_actions.add((i, j))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.

    Args:
        board (list): The current state of the board.
        action (tuple): The action to be taken.

    Returns:
        list: The new board state after applying the action.
    """
    if action not in actions(board):
        raise Exception("Invalid action")

    new_board = copy.deepcopy(board)
    i, j = action
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.

    Args:
        board (list): The current state of the board.

    Returns:
        str: The winner of the game (X or O), or None if there is no winner.
    """
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.

    Args:
        board (list): The current state of the board.

    Returns:
        bool: True if the game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if all(cell != EMPTY for row in board for cell in row):
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

    Args:
        board (list): The current state of the board.

    Returns:
        int: The utility of the board.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    Args:
        board (list): The current state of the board.

    Returns:
        tuple: The optimal action (i, j), or None if the board is terminal.
    """
    if terminal(board):
        return None

    if player(board) == X:
        value, move = max_value(board)
    else:
        value, move = min_value(board)

    return move

def max_value(board):
    """
    Determine the max value of the board, considering all possible actions of the X player.

    Args:
        board (list): The current state of the board.

    Returns:
        tuple: A tuple of the value of the board and the best action for X.
    """
    if terminal(board):
        return utility(board), None

    v = float("-inf")
    best_action = None
    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > v:
            v = min_val
            best_action = action
        if v == 1:
            break
    return v, best_action

def min_value(board):
    """
    Determine the min value of the board, considering all possible actions of the O player.

    Args:
        board (list): The current state of the board.

    Returns:
        tuple: A tuple of the value of the board and the best action for O.
    """
    if terminal(board):
        return utility(board), None

    v = float("inf")
    best_action = None
    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < v:
            v = max_val
            best_action = action
        if v == -1:
            break
    return v, best_action
