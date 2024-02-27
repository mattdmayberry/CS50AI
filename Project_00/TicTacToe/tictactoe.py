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
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Make a deep copy of the board
    new_board = copy.deepcopy(board)

    # Unpack the action
    i, j = action

    # Check if the action is valid
    if new_board[i][j] != EMPTY:
        raise Exception("Invalid action")

    # Update the board with the current player's symbol
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    # Check if the board is full (tie)
    if all(cell != EMPTY for row in board for cell in row):
        return None  # Tie

    # Game still in progress
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there is a winner
    if winner(board) is not None:
        return True

    # Check if the board is full (tie)
    if all(cell != EMPTY for row in board for cell in row):
        return True

    # Game still in progress
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Check if X has won
    if winner(board) == X:
        return 1
    # Check if O has won
    elif winner(board) == O:
        return -1
    # Game ended in a tie
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Base case: if the board is terminal, return None
    if terminal(board):
        return None

    # Initialize best move and best value
    best_move = None
    best_value = float("-inf") if player(board) == X else float("inf")

    # Loop through all possible actions
    for action in actions(board):
        # Get the utility value of the action
        value = min_value(result(board, action))

        # Update best move and best value based on player
        if player(board) == X:
            if value > best_value:
                best_value = value
                best_move = action
        else:
            if value < best_value:
                best_value = value
                best_move = action

    return best_move


def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

