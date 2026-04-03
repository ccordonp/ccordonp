"""
# # # Tic-Tac-Toe Game # # #
An e

# Code written by Claude Cordon Pichilla
# Basic Creative Commons license (free to use, publisish, modify, etc.)
"""
# Initialize the board


def initialize_board():
    """
    Initialize the board with empty spaces
    Parameters:
        None
    Returns:
        list: The board with empty spaces
    """
    return [" " for _ in range(9)]


# Display the board
def display_board(board):
    """
    Display the board on the screen
    Parameters:
        board (list): The current board
    Returns:
        None
    """
    print("\n " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")


# Check if the board is full
def is_board_full(board):
    """
    Check if the board is full (no empty spaces)
    Parameters:
        board (list): The current board
    Returns:
        bool: True if the board is full, False otherwise
    """

    # run a counter for the board up to 9
    box, full = 0, 9

    for space in board:
        if space != " ":
            box += 1
        else:
            break
    if box == full:
        return True
    else:
        return False


# Check for a win
def check_win(board, player):
    """
    Check if the player has won in any of the possible ways/conditions
    Parameters:
        board (list): The current board
        player (str): The player ("X" or "O")
    Returns:
        bool: True if the player has won, False otherwise
    """
    win = [player,player,player]

    # A list of all possible winning combinations

    winning_combos = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    # Loop through the winning combos and check if any of them matches the win list

    for combo in winning_combos:

        if [board[combo[0]], board[combo[1]], board[combo[2]]] == win:
            return True


# Get player input
def get_player_input(board, player):
    """
    Get the player's move and check if it is valid
    Parameters:
      board (list): The current board
      player (str): The player ("X" or "O")
    Returns:
      int: The position of the player's move
    """

    while True:
        print("\nThe current player is: " + player)
        move = input("Enter your move (1-9): ")

        # checks if the input is a numeral and if the corresponding space is empty.
        # if it's valid, it returns (move - 1)
        if move.isdigit():
            move = int(move)
            if 1 <= move <= 9 and board[move-1] == ' ':
                return move - 1
            else:
                print("Invalid move. Please enter a number between 1 and 9 that is not already taken.")
        else:
            print("Invalid input. Please enter a number.")


# Main game loop
def play_game():
    """
    The main game loop where the game is played until completion
    """
    board = initialize_board()
    player = "X"

    while True:
        display_board(board)
        move = get_player_input(board, player=player)
        board[move] = player
        if check_win(board,player) is True:
            display_board(board)
            print("Winner Winner Chicken Dinner")
            break

        # Note: this portion has been comppleted for you
        if is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"


# Start the game
# this is the main function, and you do not need to make any changes here
if __name__ == "__main__":
    play_game()