"Calculates if the Game State is winning or not"
def win(board, player):
    "calculates if a player won on the board"
    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Diagonal \
    if all(board[i][i] == player for i in range(3)):
        return True

    # Diagonal /
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def gamestate(board):
    "calculate the Game State"
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)

    # Validate move counts
    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")

    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")

    winner_x = win(board, "X")
    winner_o = win(board, "O")

    # Both cannot win
    if winner_x and winner_o:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    # X can only win after making the extra move
    if winner_x or winner_o:
        return "win"

    if x_count + o_count == 9:
        return "draw"

    return "ongoing"