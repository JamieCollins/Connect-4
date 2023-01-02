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


def user_col_guess():
    """
    Asks user to choose a column on the grid in which to drop a token,
    - 1 is taken from selection for indexing purposes.
    """
    print("\nYour opponent just placed a token, it's now your turn:")
    global col
    col = (int(input
            ("Choose a row by entering a number between 1 and 7: ")) - 1)
    verify_user_placement()


def verify_user_placement():
    """
    Verifies the placement of the tokens on the board for the user.
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


def verify_ai_placement():
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


def game_fin_user():
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
    Ends game if either users matches 4 tokens. Asks if user would
    like to replay and resets grid if so.
    """
    if game_fin_user() or game_fin_ai() == True:
        print("Game Over")
        user_replay_input = (input("Would you like to play again? (y/n): "))
        if user_replay_input == "y":
            global game_grid
            game_grid = [[".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],]
            game_start()
        elif user_replay_input == "n":
            print("Goodbye!")
        else:
            print("please type 'y' or 'n':")
            user_replay_input = (input("Would you like to play again? (y/n): "))
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
        user_col_guess()
    else:
        verify_ai_placement()

game_start()