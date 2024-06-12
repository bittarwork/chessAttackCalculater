def load_chess_board(filename):
    """
    Loads a chess board configuration from a text file.

    Parameters:
    filename (str): The name of the file to read from.

    Returns:
    list: A 2D list representing the chess board.
    """
    with open(filename) as file:
        return [['Empty' if char == '0' else char for char in line.split()] for line in file]


def mark_rook_attacks(board):
    """
    Marks squares attacked by rooks on the board.

    Parameters:
    board (list): A 2D list representing the chess board.

    Returns:
    list: A 2D list with attacked squares marked as -1.
    """
    size = len(board)
    threat_map = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'R':
                for k in range(size):
                    threat_map[i][k] = -1
                    threat_map[k][j] = -1
    return threat_map


def mark_bishop_attacks(board):
    """
    Marks squares attacked by bishops on the board.

    Parameters:
    board (list): A 2D list representing the chess board.

    Returns:
    list: A 2D list with attacked squares marked as -1.
    """
    size = len(board)
    threat_map = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'B':
                for d in range(1, size):
                    if i - d >= 0 and j - d >= 0:
                        threat_map[i - d][j - d] = -1
                    if i + d < size and j + d < size:
                        threat_map[i + d][j + d] = -1
                    if i - d >= 0 and j + d < size:
                        threat_map[i - d][j + d] = -1
                    if i + d < size and j - d >= 0:
                        threat_map[i + d][j - d] = -1
    return threat_map


def mark_queen_attacks(board):
    """
    Marks squares attacked by queens on the board.

    Parameters:
    board (list): A 2D list representing the chess board.

    Returns:
    list: A 2D list with attacked squares marked as -1.
    """
    size = len(board)
    threat_map = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'Q':
                for k in range(size):
                    threat_map[i][k] = -1
                    threat_map[k][j] = -1
                for d in range(1, size):
                    if i - d >= 0 and j - d >= 0:
                        threat_map[i - d][j - d] = -1
                    if i + d < size and j + d < size:
                        threat_map[i + d][j + d] = -1
                    if i - d >= 0 and j + d < size:
                        threat_map[i - d][j + d] = -1
                    if i + d < size and j - d >= 0:
                        threat_map[i + d][j - d] = -1
    return threat_map


def calculate_attacked_squares(board):
    """
    Calculates the number of squares attacked by all pieces on the board.

    Parameters:
    board (list): A 2D list representing the chess board.

    Returns:
    int: The number of squares under attack.
    """
    rook_threats = mark_rook_attacks(board)
    bishop_threats = mark_bishop_attacks(board)
    queen_threats = mark_queen_attacks(board)
    size = len(board)
    total_threats = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if rook_threats[i][j] == -1 or bishop_threats[i][j] == -1 or queen_threats[i][j] == -1:
                total_threats[i][j] = -1
    return sum(row.count(-1) for row in total_threats)


def calculate_safe_squares(board):
    """
    Calculates the number of safe squares on the board.

    Parameters:
    board (list): A 2D list representing the chess board.

    Returns:
    int: The number of squares that are not under attack.
    """
    total_squares = len(board) ** 2
    return total_squares - calculate_attacked_squares(board)


def compute_chess_board_stats(board):
    """
    Computes and prints the number of attacked and safe squares on the board.

    Parameters:
    board (list): A 2D list representing the chess board.
    """
    attacked = calculate_attacked_squares(board)
    safe = calculate_safe_squares(board)
    print({"attacked_squares": attacked, "safe_squares": safe})


def mark_knight_attacks(board):
    """
    Marks squares attacked by knights on the board.

    Parameters:
    board (list): A 2D list representing the chess board.

    Returns:
    list: A 2D list with attacked squares marked as -1.
    """
    size = len(board)
    threat_map = [[0] * size for _ in range(size)]
    knight_moves = [
        (-2, -1), (-2, 1), (2, -1), (2, 1),
        (-1, -2), (-1, 2), (1, -2), (1, 2)
    ]
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'N':
                for move in knight_moves:
                    ni, nj = i + move[0], j + move[1]
                    if 0 <= ni < size and 0 <= nj < size:
                        threat_map[ni][nj] = -1
    return threat_map


def mark_king_attacks(board):
    """
    Marks squares attacked by kings on the board.

    Parameters:
    board (list): A 2D list representing the chess board.

    Returns:
    list: A 2D list with attacked squares marked as -1.
    """
    size = len(board)
    threat_map = [[0] * size for _ in range(size)]
    king_moves = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                for move in king_moves:
                    ni, nj = i + move[0], j + move[1]
                    if 0 <= ni < size and 0 <= nj < size:
                        threat_map[ni][nj] = -1
    return threat_map


def mark_pawn_attacks(board):
    """
    Marks squares attacked by pawns on the board.

    Parameters:
    board (list): A 2D list representing the chess board.

    Returns:
    list: A 2D list with attacked squares marked as -1.
    """
    size = len(board)
    threat_map = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'P':
                if i - 1 >= 0:
                    if j - 1 >= 0:
                        threat_map[i - 1][j - 1] = -1
                    if j + 1 < size:
                        threat_map[i - 1][j + 1] = -1
    return threat_map


def calculate_attacked_squares(board):
    """
    Calculates the number of squares attacked by all pieces on the board.

    Parameters:
    board (list): A 2D list representing the chess board.

    Returns:
    int: The number of squares under attack.
    """
    size = len(board)
    threat_maps = [
        mark_rook_attacks(board),
        mark_bishop_attacks(board),
        mark_queen_attacks(board),
        mark_knight_attacks(board),
        mark_king_attacks(board),
        mark_pawn_attacks(board)
    ]
    total_threats = [[0] * size for _ in range(size)]
    for threat_map in threat_maps:
        for i in range(size):
            for j in range(size):
                if threat_map[i][j] == -1:
                    total_threats[i][j] = -1
    return sum(row.count(-1) for row in total_threats)


def compute_chess_board_stats(board):
    """
    Computes and prints the number of attacked and safe squares on the board.

    Parameters:
    board (list): A 2D list representing the chess board.
    """
    attacked = calculate_attacked_squares(board)
    total_squares = len(board) ** 2
    safe = total_squares - attacked
    print({"attacked_squares": attacked, "safe_squares": safe})


chess_board = load_chess_board("board.txt")
compute_chess_board_stats(chess_board)
