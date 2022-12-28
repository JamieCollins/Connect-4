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
    col = int(input("Please enter a number between 0 and 6: "))
    verify_token_placement()


def reset_row_counter():
    """
    Resets row counter for token placements.
    """


def verify_token_placement():
    """
    Verifies the placement of the tokens on the board.
    """
    global rows
    if game_grid[rows][col] == ".":
        game_grid[rows][col] = "O"
        create_game_board()
        player_guess()
    elif game_grid[rows][col] != ".":
        rows = rows - 1
        game_grid[rows][col] = "O"
        create_game_board()
        player_guess()
    else:
        print("ERROR")
    


def game_start():
    player_guess()

game_start()