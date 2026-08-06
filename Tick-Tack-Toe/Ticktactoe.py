import sys

def print_board(board: list[list[str]]):
    """Prints the current 3x3 game board nicely."""
    print("\n")
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---+---+---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---+---+---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print("\n")


def check_win(board: list[list[str]], player: str) -> bool:
    """Checks rows, columns, and diagonals for 3 matching symbols."""
    # 1. Check Rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    # 2. Check Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # 3. Check Diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def check_draw(board: list[list[str]]) -> bool:
    """Checks if all board positions are filled without a winner."""
    for row in board:
        for cell in row:
            if cell not in ['X', 'O']:
                return False
    return True


def get_move(player: str, board: list[list[str]]) -> tuple[int, int]:
    """Gets and validates a row/col choice from the user."""
    while True:
        user_input = input(f"Player {player}, enter position (1-9) or 'exit': ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            sys.exit()

        if not user_input.isdigit():
            printInvalid input! Please enter a number between 1 and 9.")
            continue

        pos = int(user_input)
        if pos < 1 or pos > 9:
            print("Please choose a number from 1 to 9.")
            continue

        # Convert 1-9 to row and column indices
        row = (pos - 1) // 3
        col = (pos - 1) % 3

        if board[row][col] in ['X', 'O']:
            print("❌ That spot is already taken! Choose another spot.")
            continue

        return row, col


def play_game():
    print("=== Python Tic-Tac-Toe ===")
    print("Positions are mapped 1-9 like this:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("Type 'exit' at any prompt to quit.\n")

    # Initialize empty board grid
    board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

    current_player = "X"

    while True:
        print_board(board)
        row, col = get_move(current_player, board)

        # Place player's mark
        board[row][col] = current_player

        # Check for Win
        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 CONGRATULATIONS! Player {current_player} wins!\n")
            break

        # Check for Draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!\n")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()    
