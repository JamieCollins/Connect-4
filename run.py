def create_game_board():
    """
    Creates a table of 6 rows and 7 columns to be used as the game board.
    """
    for i in range(6):
            for j in range(7):
                print(". ", end="")

            print()


create_game_board()


def player_guess():
    player_column_select = int(input("Please enter a number between 0 and 6: "))
    print(player_column_select)

player_guess()