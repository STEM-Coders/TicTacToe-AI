"""
Tic Tac Toe Player
"""

import math, copy

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

    x, o = 0, 0

    for i in board:
        for j in i:
            if j == X:
                x += 1
            elif j == O:
                o += 1

    if x == o:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    action = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                action.append((i, j))

    return action

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    newBoard = copy.deepcopy(board)

    if newBoard[action[0]][action[1]] != EMPTY:
        raise NameError('Envalid action')


    newBoard[action[0]][action[1]] = player(board)

    return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if utility(board) == 1:
        return X
    if utility(board) == -1:
        return O

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True

    for i in board:
        for j in i:
            if j == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # Checks for all horizontal 3 in rows
    if board[0][0] == X and board[0][1] == X and board[0][2] == X:
        return 1
    if board[0][0] == O and board[0][1] == O and board[0][2] == O:
        return -1

    if board[1][0] == X and board[1][1] == X and board[1][2] == X:
        return 1
    if board[1][0] == O and board[1][1] == O and board[1][2] == O:
        return -1

    if board[2][0] == X and board[2][1] == X and board[2][2] == X:
        return 1
    if board[2][0] == O and board[2][1] == O and board[2][2] == O:
        return -1

    # Checks all vertical 3 in rows
    if board[0][0] == X and board[1][0] == X and board[2][0] == X:
        return 1
    if board[0][0] == O and board[1][0] == O and board[2][0] == O:
        return -1

    if board[0][1] == X and board[1][1] == X and board[2][1] == X:
        return 1
    if board[0][1] == O and board[1][1] == O and board[2][1] == O:
        return -1

    if board[0][2] == X and board[1][2] == X and board[2][2] == X:
        return 1
    if board[0][2] == O and board[1][2] == O and board[2][2] == O:
        return -1

    # Checks all diagnal wins
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return 1
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return -1

    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return 1
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return -1

    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def Max_value(s):
        if terminal(s):
            return utility(s)
        v = -2
        for a in actions(s):
            v = max(v, Min_value(result(s, a)))
        return v

    def Min_value(s):
        if terminal(s):
            return utility(s)
        v = 2
        for a in actions(s):
            v = min(v, Max_value(result(s, a)))
        return v

    if terminal(board):
        return None
    elif player(board) == X:
        v = -2
        move = ()
        for a in actions(board):
            x = Max_value(result(board, a))
            if x > v:
                v = x
                move = a
        return move
    else:
        v = 2
        move = ()
        for a in actions(board):
            x = Min_value(result(board, a))
            if x < v:
                v = x
                move = a
        return move
