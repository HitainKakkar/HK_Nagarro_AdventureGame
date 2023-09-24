import time
import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if the game is over
def is_game_over(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True

    for col in range(3):
        check = [board[row][col] for row in range(3)]
        if check.count(check[0]) == 3 and check[0] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

# Function to make the player's move
def player_move(board, row, col):
    if board[row][col] == " ":
        board[row][col] = "X"
        return True
    else:
        return False

# Function for the computer's move (random)
def computer_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"

# Function to play the Tic-Tac-Toe game and return the result
def play_tic_tac_toe():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]

    # Main game loop
    while True:
        print_board(board)

        # Player's move
        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if player_move(board, row, col):
                        break
                    else:
                        print("That cell is already occupied. Try again.")
                else:
                    print("Invalid input. Please enter a number between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 2.")

        if is_game_over(board):
            print_board(board)
            print("Congratulations! You win!")
            time.sleep(1)
            return 0  # User wins

        # Computer's move
        computer_move(board)

        if is_game_over(board):
            print_board(board)
            print("Computer wins. Better luck next time!")
            time.sleep(1)
            return 1  # User loses

        # Check for a tie
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a tie!, but I declare you win")
            time.sleep(1)
            return 1  # It's a tie

# Call the function to play the game
# result = play_tic_tac_toe()
# print("Game result:", result)
