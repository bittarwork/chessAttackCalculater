import random


def generate_random_chess_board():
    """
    Generates a random chess board configuration.

    Returns:
    list: A 2D list representing the chess board.
    """
    pieces = ['R', 'N', 'B', 'Q', 'K', 'P', 'r', 'n', 'b', 'q', 'k', 'p']
    empty_squares = 64 - len(pieces)

    # Create a flat list with the pieces and empty squares
    board_list = pieces + ['0'] * empty_squares

    # Shuffle the list to randomize positions
    random.shuffle(board_list)

    # Convert the flat list to a 2D list
    board = [board_list[i:i+8] for i in range(0, 64, 8)]

    return board


def save_chess_board(filename, board):
    """
    Saves the chess board configuration to a text file.

    Parameters:
    filename (str): The name of the file to write to.
    board (list): A 2D list representing the chess board.
    """
    with open(filename, 'w') as file:
        for row in board:
            file.write(' '.join(row) + '\n')


def main():
    for i in range(50):
        board = generate_random_chess_board()
        save_chess_board(f'board{i}.txt', board)


if __name__ == "__main__":
    main()
