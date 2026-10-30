def display_board(board):
    """Print the current board."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def has_winner(board, player):
    """Return True when the player has three matching spaces."""
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for combination in winning_combinations:
        if all(board[position] == player for position in combination):
            return True

    return False


def board_is_full(board):
    """Return True when there are no empty spaces left."""
    return all(space in ("X", "O") for space in board)


def play_game():
    """Run one game of tic-tac-toe."""
    board = [str(number) for number in range(1, 10)]
    current_player = "X"

    print("Tic-Tac-Toe")
    print("Choose a position from 1 to 9.")

    while True:
        display_board(board)
        choice = input(f"Player {current_player}, choose a position: ")

        if not choice.isdigit() or int(choice) not in range(1, 10):
            print("Please enter a number from 1 to 9.")
            continue

        position = int(choice) - 1

        if board[position] in ("X", "O"):
            print("That position is already taken.")
            continue

        board[position] = current_player

        if has_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if board_is_full(board):
            display_board(board)
            print("It's a draw!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


if __name__ == "__main__":
    play_game()
