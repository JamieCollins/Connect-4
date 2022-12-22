rows = 6
cols = 7


#def create_game_board():
#   """
#   Creates a table of 6 rows and 7 columns to be used as the game board.
#   """
#  for i in range(rows):
#          for j in range(cols):
#               print(". ", end="")
#
#           print()


game_grid = [[". ", ". ", ". ", ". ", ". ", ". ", ". "],
            [". ", ". ", ". ", ". ", ". ", ". ", ". "],
            [". ", ". ", ". ", ". ", ". ", ". ", ". "],
            [". ", ". ", ". ", ". ", ". ", ". ", ". "],
            [". ", ". ", ". ", ". ", ". ", ". ", ". "],
            [". ", ". ", ". ", ". ", ". ", ". ", ". "],]

def create_game_board():
    """
    Creates a table of 6 rows and 7 columns to be used as the game board.
    """
    for i in game_grid:
        print(*i)


def player_guess():
    col = int(input("Please enter a number between 0 and 6: "))
    game_grid[5][col] = "O"
    create_game_board()


player_guess()