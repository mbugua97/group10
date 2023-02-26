# Define the TicTacToe board as a dictionary with keys 1-9
# and values initially set to a space character
board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

# Function to print the TicTacToe board
def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

# Function to check if a player has won or if the game is a tie
def check_win(board):
    # Define all possible win combinations as a list of lists
    win_combinations = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['1', '4', '7'],
        ['2', '5', '8'],
        ['3', '6', '9'],
        ['1', '5', '9'],
        ['3', '5', '7']
    ]

    # Check each win combination to see if a player has won
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]

    # If no player has won and there are no empty spaces left, the game is a tie
    if ' ' not in board.values():
        return 'tie'

    # If the game is still ongoing, return None
    return None

# Function to get a player's move and update the board
def get_move(board, player):
    # Loop until a valid move is entered or the player types 'exit'
    while True:
        move = input(f"{player}, enter a number from 1-9 to make your move (or type 'exit' to quit): ")
        if move == 'exit':
            print("Thanks for playing!. Hope to see you soon!!")
            exit()
        elif move not in board.keys() or board[move] != ' ':
            print("Invalid move, please try again.")
        else:
            # If the move is valid, update the board and exit the loop
            board[move] = player
            break

# Function to play a full game of TicTacToe
def play_game():
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X")
    print("Player 2: O")
    print_board(board)
    current_player = 'X'
    # Loop until a player wins or the game is a tie
    while True:
        get_move(board, current_player)
        print_board(board)
        winner = check_win(board)
        if winner:
            if winner == 'tie':
                print("It's a tie!")
            else:
                print(f"{winner} wins!. Nice Moves There!!")
            return
        # Switch the current player after each turn
        current_player = 'O' if current_player == 'X' else 'X'

# Call the play_game function to start the game
play_game()