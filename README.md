# Chessboard Threat and Safe Squares Calculator

This project calculates the number of squares attacked and the number of safe squares on a chessboard based on the positions of various chess pieces. The project is implemented in Python.

## Features

- Load a chessboard configuration from a text file
- Calculate and mark squares attacked by:
  - Rooks
  - Bishops
  - Queens
  - Knights
  - Kings
  - Pawns
- Compute the total number of attacked and safe squares on the board

## Usage

1. **Load Chess Board Configuration**

    The chessboard configuration should be stored in a text file (`board.txt`) where each piece is represented by a single character and empty squares are represented by `0`. Each row of the chessboard is a separate line in the file.

    Example of `board.txt`:
    ```
    R 0 0 0 0 0 0 R
    0 0 0 0 0 0 0 0
    0 0 0 B 0 0 0 0
    0 0 0 0 0 0 N 0
    0 0 0 0 Q 0 0 0
    0 P 0 0 0 0 0 0
    0 0 0 0 0 0 0 0
    r 0 0 0 0 0 0 r
    ```

2. **Run the Script**

    The script reads the chessboard configuration, calculates the attacked and safe squares, and prints the results.

    ```python
    chess_board = load_chess_board("board.txt")
    compute_chess_board_stats(chess_board)
    ```

## Functions

- `load_chess_board(filename)`: Loads a chessboard configuration from a text file.
- `mark_rook_attacks(board)`: Marks squares attacked by rooks.
- `mark_bishop_attacks(board)`: Marks squares attacked by bishops.
- `mark_queen_attacks(board)`: Marks squares attacked by queens.
- `mark_knight_attacks(board)`: Marks squares attacked by knights.
- `mark_king_attacks(board)`: Marks squares attacked by kings.
- `mark_pawn_attacks(board)`: Marks squares attacked by pawns.
- `calculate_attacked_squares(board)`: Calculates the number of squares attacked by all pieces.
- `compute_chess_board_stats(board)`: Computes and prints the number of attacked and safe squares.

## Example Output

Running the script with the provided `board.txt` might produce an output like:

```json
{
    "attacked_squares": 24,
    "safe_squares": 40
}
