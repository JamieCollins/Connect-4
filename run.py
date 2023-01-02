from random import randint

game_grid = [[".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],]

rows = 5
turn = 0


def create_game_board():
    """
    Creates a table of 6 rows and 7 columns to be used as the game board.
    """
    for i in game_grid:
        print(*i)


def player_guess():
    """
    Asks user to choose a column on the grid in which to drop a token,
    - 1 is taken from selection for indexing purposes.
    """
    global col
    col = (int(input("Please enter a number between 1 and 7: ")) - 1)
    verify_token_placement()


def verify_token_placement():
    """
    Verifies the placement of the tokens on the board for the player.
    """
    global rows
    if game_grid[rows][col] == ".":
        game_grid[rows][col] = "O"
        create_game_board()
        end_game()
    elif game_grid[rows - 1][col] == ".":
        game_grid[rows - 1][col] = "O"
        create_game_board()
        end_game()
    elif game_grid[rows - 2][col] == ".":
        game_grid[rows - 2][col] = "O"
        create_game_board()
        end_game()
    elif game_grid[rows - 3][col] == ".":
        game_grid[rows - 3][col] = "O"
        create_game_board()
        end_game()
    elif game_grid[rows - 4][col] == ".":
        game_grid[rows - 4][col] = "O"
        create_game_board()
        end_game()
    elif game_grid[rows - 5][col] == ".":
        game_grid[rows - 5][col] = "O"
        create_game_board()
        end_game()
    else:
        print("ERROR")
    

def player_2_guess():
    """
    Verifies the placement of the tokens on the board for the ai,
    randint is used to choose a random row.
    """
    print("\n")
    global rows
    col = randint(0, 6)
    if game_grid[rows][col] == ".":
        game_grid[rows][col] = "X"
        create_game_board()
        end_game()
    elif game_grid[rows - 1][col] == ".":
        game_grid[rows - 1][col] = "X"
        create_game_board()
        end_game()
    elif game_grid[rows - 2][col] == ".":
        game_grid[rows - 2][col] = "X"
        create_game_board()
        end_game()
    elif game_grid[rows - 3][col] == ".":
        game_grid[rows - 3][col] = "X"
        create_game_board()
        end_game()
    elif game_grid[rows - 4][col] == ".":
        game_grid[rows - 4][col] = "X"
        create_game_board()
        end_game()
    elif game_grid[rows - 5][col] == ".":
        game_grid[rows - 5][col] = "X"
        create_game_board()
        end_game()
    else:
        print("ERROR")


def game_fin():
    """
    Checks to see if user player has ammassed 4 tokens either
    horizontally, vertically or diagonally.
    """
    for col in range(7):
        for rows in range(6):
            if (game_grid[rows][col] == "O"
                and game_grid[rows - 1][col] == "O"
                    and game_grid[rows - 2][col] == "O"
                        and game_grid[rows - 3][col] == "O"):
                            print("Congratulations, you won vertically!")
                            return True
            elif (game_grid[rows][col] == "O"
                and game_grid[rows][col - 1] == "O"
                    and game_grid[rows][col - 2] == "O"
                        and game_grid[rows][col - 3] == "O"):
                            print("Congratulations, you won horizontally!")
                            return True
            elif (game_grid[rows][col] == "O"
                and game_grid[rows - 1][col - 1] == "O"
                    and game_grid[rows - 2][col - 2] == "O"
                        and game_grid[rows - 3][col - 3] == "O"):
                            print("Congratulations, you won diagonally!")
                            return True


def game_fin_ai():
    """
    Checks to see if the AI opponent has ammassed 4 tokens either
    horizontally, vertically or diagonally.
    """
    for col in range(7):
        for rows in range(6):
            if (game_grid[rows][col] == "X"
                and game_grid[rows - 1][col] == "X"
                    and game_grid[rows - 2][col] == "X"
                        and game_grid[rows - 3][col] == "X"):
                            print("Unfortunately you lost!")
                            return True
            elif (game_grid[rows][col] == "X"
                and game_grid[rows][col - 1] == "X"
                    and game_grid[rows][col - 2] == "X"
                        and game_grid[rows][col - 3] == "X"):
                            print("Unfortunately you lost!")
                            return True
            elif (game_grid[rows][col] == "O"
                and game_grid[rows - 1][col - 1] == "X"
                    and game_grid[rows - 2][col - 2] == "X"
                        and game_grid[rows - 3][col - 3] == "X"):
                            print("Unfortunately you lost!")
                            return True


def end_game():
    """
    Ends game if either users matches 4 tokens.
    """
    if game_fin() or game_fin_ai() == True:
        print("Game Over")
    else:
        game_start()


def game_start():
    """
    Initialises game turn. If number is odd, player chooses a row to drop token,
    if even it is the cpu's turn.
    """
    global turn
    turn = turn + 1
    if turn % 2 == 0:
        player_guess()
    else:
        player_2_guess()

game_start()