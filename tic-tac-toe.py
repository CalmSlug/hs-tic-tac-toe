board = "         "
turn_counter = 0
player = "X"
X_win = 0
O_win = 0

print("---------")
print("| " + board[0] + " " + board[1] + " " + board[2] + " |")
print("| " + board[3] + " " + board[4] + " " + board[5] + " |")
print("| " + board[6] + " " + board[7] + " " + board[8] + " |")
print("---------")

while True:
    move = input("Enter the coordinates: ")

    if move.isalpha():
        print("You should enter numbers!")
        pass

    else:
        move_row, move_col = move.split()
        move_x = int(move_row) - 1
        move_y = 3 - int(move_col)
        index = move_x + (move_y * 3)

        if 1 <= int(move_row) <= 3 and 1 <= int(move_col) <= 3:

            if board[index] != " ":
                print("This cell is occupied! Choose another one!")
                pass

            else:
                board_list = list(board)
                board_list[index] = player
                board = "".join(board_list)
                print("---------")
                print("| " + board[0] + " " + board[1] + " " + board[2] + " |")
                print("| " + board[3] + " " + board[4] + " " + board[5] + " |")
                print("| " + board[6] + " " + board[7] + " " + board[8] + " |")
                print("---------")
                turn_counter += 1
                
                if board[0] == "X" and board[3] == "X" and board[6] == "X":
                    X_win += 1
                elif board[1] == "X" and board[4] == "X" and board[7] == "X":
                    X_win += 1
                elif board[2] == "X" and board[5] == "X" and board[8] == "X":
                    X_win += 1
                elif board[0] == "X" and board[1] == "X" and board[2] == "X":
                    X_win += 1
                elif board[3] == "X" and board[4] == "X" and board[5] == "X":
                    X_win += 1
                elif board[6] == "X" and board[7] == "X" and board[8] == "X":
                    X_win += 1
                elif board[0] == "X" and board[4] == "X" and board[8] == "X":
                    X_win += 1
                elif board[2] == "X" and board[4] == "X" and board[6] == "X":
                    X_win += 1
                if board[0] == "O" and board[3] == "O" and board[6] == "O":
                    O_win += 1
                elif board[1] == "O" and board[4] == "O" and board[7] == "O":
                    O_win += 1
                elif board[2] == "O" and board[5] == "O" and board[8] == "O":
                    O_win += 1
                elif board[0] == "O" and board[1] == "O" and board[2] == "O":
                    O_win += 1
                elif board[3] == "O" and board[4] == "O" and board[5] == "O":
                    O_win += 1
                elif board[6] == "O" and board[7] == "O" and board[8] == "O":
                    O_win += 1
                elif board[0] == "O" and board[4] == "O" and board[8] == "O":
                    O_win += 1
                elif board[2] == "O" and board[4] == "O" and board[6] == "O":
                    O_win += 1

                if X_win == 1:
                    print("X wins")
                    break
                if O_win == 1:
                    print("O wins")
                    break
                if turn_counter == 9 and X_win == 0 and O_win == 0:
                    print("Draw")
                    break
                
                if player == "X":
                    player = "O"
                else:
                    player = "X"
        else:
            print("Coordinates should be from 1 to 3!")
            pass