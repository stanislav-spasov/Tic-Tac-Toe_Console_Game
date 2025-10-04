def print_board(current_board):
    for r in current_board:
        print(f"| {' | '.join(r)} |")


def row_winner(current_board, sign):
    for r in current_board:
        counter = r.count(sign)
        if counter == 3:
            return True
    return False


def col_winner(current_board, sign):
    for c in range(3):
        counter = 0
        for r in range(3):
            if current_board[r][c] == sign:
                counter += 1
        if counter == 3:
            return True
    return False


def diagonal_winner(current_board, sign):
    primary_counter = 0
    secondary_counter = 0
    for i in range(3):
        if current_board[i][i] == sign:
            primary_counter += 1
        if current_board[i][-i - 1] == sign:
            secondary_counter += 1
    if primary_counter == 3 or secondary_counter == 3:
        return True
    return False


def chek_for_winner(current_board, sign):
    if row_winner(current_board, sign) or col_winner(current_board, sign) or diagonal_winner(current_board, sign):
        return True
    return False


player_one = input("Player one name: ")
player_two = input("Player two name: ")

player_one_sign = input(f"{player_one} would you like to play with 'X' or 'O'? ").upper()

while player_one_sign not in ["X", "O"]:
    print(f"Please enter either 'X' or 'O'.")
    player_one_sign = input(f"{player_one} would you like to play with 'X' or 'O'? ").upper()

player_two_sign = "O" if player_one_sign == "X" else "X"

print("This is the numeration of the board:")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")
print(f"{player_one} starts first!")

game_board = [[" ", " ", " "] for i in range(3)]

mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}

turns = 1

while turns <= 9:
    current_player = player_one if turns % 2 != 0 else player_two
    current_sign = player_one_sign if turns % 2 != 0 else player_two_sign
    try:
        position = int(input(f"{current_player} chose a free position [1-9]: "))
    except ValueError:
        print("Please enter a number between 1 and 9.")
        continue

    if position < 1 or position > 9 or position < 0:
        print("Please enter a number between 1 and 9.")
        continue

    row, col = mapper[position]
    if game_board[row][col] != " ":
        print("Please choice a free position.")
        continue
    else:
        game_board[row][col] = current_sign

    turns += 1

    print_board(game_board)

    if turns > 5 and chek_for_winner(game_board, current_sign):
        print(f"Congratulations, {current_player} won!")
        break

else:
    print("Thanks for playing! No winner today!")
