# Tic-Tac-Toe game implementation

# Function to print the board
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

# Function to check if a player has won
def check_win(board, player):
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to check if the board is full (no empty spaces)
def is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

# Main function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}, it's your turn!")
        
        # Get player input
        while True:
            try:
                row, col = map(int, input("Enter row and column (0, 1, or 2) separated by a space: ").split())
                if board[row][col] != " ":
                    print("This position is already taken. Try again.")
                else:
                    board[row][col] = current_player
                    break
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column values between 0 and 2.")
        
        # Check for win or tie
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    play_game()
