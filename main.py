# Function to convert a board for dictionary
def convert_to_dict(board):
    flattened_board = "".join(["".join(row) for row in board])
    return {i: flattened_board[i-1] for i in range(1, len(flattened_board) + 1)}


# Function for printing board
def print_board(board_dict):
    for i in range(1, 10):
        if i % 3 != 0:
            print(" {} |".format(board_dict[i]), end="")
        else:
            print(" {}".format(board_dict[i]))

        if i % 3 == 0 and i != 9:
            print("-----------")


board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
board_dict = convert_to_dict(board)


def check_winner(board_dict):
    # Checking all possibles wining lines
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Horizontal lines
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Vertical lines
        [1, 5, 9], [3, 5, 7]  # Diagonals lines
    ]

    for condition in win_conditions:
        if board_dict[condition[0]] == board_dict[condition[1]] == board_dict[condition[2]] != " ":
            return True  # There is a winner
    return False  # There is no winner


def check_draw(board_dict):
    # Checking if board is full
    return all(value != " " for value in board_dict.values())


current_player = "X"
game_over = False

while not game_over:

    # Printing the board game
    print_board(board_dict)

    # Taking the move from current player
    move = input("Player {}, chose your position (1-9): ".format(current_player))

    # Actualisation of board game based on move
    if board_dict[int(move)] == " ":
        board_dict[int(move)] = current_player
    else:
        print("This position is occupied")

    # Checking the end game rules
    if check_winner(board_dict):
        print_board(board_dict)
        print("Player {} have won.".format(current_player))
        game_over = True
    elif check_draw(board_dict):
        print_board(board_dict)
        print("It's draw")
        game_over = True
    else:
        # Change the player
        current_player = "O" if current_player == "X" else "X"

