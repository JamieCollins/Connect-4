#def create_game_board():
#   """
#   Creates a table of 6 rows and 7 columns to be used as the game board.
#   """
#  for i in range(rows):
#          for j in range(cols):
#               print(". ", end="")
#
#           print()


game_grid = [[".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],]

rows = 5

def create_game_board():
    """
    Creates a table of 6 rows and 7 columns to be used as the game board.
    """
    for i in game_grid:
        print(*i)


def player_guess():
    """
    Asks user to choose a column on the grid in which to drop a token.
    """
    global col
    col = (int(input("Please enter a number between 1 and 7: ")) - 1)
    verify_token_placement()


def verify_token_placement():
    """
    Verifies the placement of the tokens on the board.
    """
    global rows
    if game_grid[rows][col] == ".":
        game_grid[rows][col] = "O"
        create_game_board()
        player_guess()
    elif game_grid[rows - 1][col] == ".":
        game_grid[rows - 1][col] = "O"
        create_game_board()
        player_guess()
    elif game_grid[rows - 2][col] == ".":
        game_grid[rows - 2][col] = "O"
        create_game_board()
        player_guess()
    elif game_grid[rows - 3][col] == ".":
        game_grid[rows - 3][col] = "O"
        create_game_board()
        player_guess()
    elif game_grid[rows - 4][col] == ".":
        game_grid[rows - 4][col] = "O"
        create_game_board()
        player_guess()
    elif game_grid[rows - 5][col] == ".":
        game_grid[rows - 5][col] = "O"
        create_game_board()
        player_guess()
    else:
        print("ERROR")
    


def game_start():
    player_guess()

game_start()