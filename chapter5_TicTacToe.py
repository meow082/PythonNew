row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']   #4, 5, 6 => row2 index 0, 1, 2
row3 = [' ', ' ', ' ']
counter = 0


def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


def user_choice():
    choice = input("Please enter a number (1-9): ")
    while not choice.isdigit() or int(choice) not in range(1, 10):
        if not choice.isdigit():
            print("Sorry, invalid choice. ")
        else:
            print("Sorry, out of range. ")
        choice = input("Please enter a number (1-9): ")
    return int(choice)


def getCurrentSymbol():
    global counter
    symbol_list = ['X', 'O']
    counter += 1
    return symbol_list[counter % 2]


def update_table(index):
    global row1, row2, row3
    if index in range(1, 4):
        if row1[index - 1] == " ":
            row1[index - 1] = getCurrentSymbol()  # 把O或X放進去
            return True
        return False
    elif index in range(4, 7):
        if row2[index - 4] == " ":
            row2[index - 4] = getCurrentSymbol()
            return True
        return False
    else:
        if row3[index - 7] == " ":
            row3[index - 7] = getCurrentSymbol()
            return True
        return False


def check_winning():
    player_1_wins = False
    player_2_wins = False
    if (row1[0] == row1[1] and row1[1] == row1[2] and " " not in row1):
        if row1[0] == 'X':
            player_1_wins = True
        else:
            player_2_wins = True
    elif (row2[0] == row2[1] and row2[1] == row2[2] and " " not in row2):
        if row2[0] == 'X':
            player_1_wins = True
        else:
            player_2_wins = True
    elif (row3[0] == row3[1] and row3[1] == row3[2] and " " not in row3):
        if row3[0] == 'X':
            player_1_wins = True
        else:
            player_2_wins = True
    elif (row1[0] == row2[0] and row2[0] == row3[0] and (row1[0] != " ")):
        if row1[0] == 'X':
            player_1_wins = True
        else:
            player_2_wins = True
    elif (row1[1] == row2[1] and row2[1] == row3[1] and (row1[1] != " ")):
        if row1[1] == 'X':
            player_1_wins = True
        else:
            player_2_wins = True
    elif (row1[2] == row2[2] and row2[2] == row3[2] and (row1[2] != " ")):
        if row1[2] == 'X':
            player_1_wins = True
        else:
            player_2_wins = True
    elif (row1[0] == row2[1] and row2[1] == row3[2] and (row1[0] != " ")):
        if row1[0] == 'X':
            player_1_wins = True
        else:
            player_2_wins = True
    elif (row1[2] == row2[1] and row2[1] == row3[0] and (row1[2] != " ")):
        if row1[2] == 'X':
            player_1_wins = True
        else:
            player_2_wins = True

    if player_1_wins:
        return "Player 1 wins!"
    elif player_2_wins:
        return "Player 2 wins!"
    else:
        return "No one wins!"


def start_game():
    global counter
    while True:
        display(row1, row2, row3)
        while True:
            choice_index = user_choice()
            if update_table(choice_index):
                break
            else:
                print("Sorry, the position is already taken. ")

        result = check_winning()
        if result != "No one wins!":
            display(row1, row2, row3)
            print(result + "!! Congrats!!")
            return     
        elif counter == 9:
            display(row1, row2, row3)
            print("It's a tie!!")
            return



start_game()