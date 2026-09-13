print("Welcome to Tic-Tac-Toe!")

board = ["1","2","3","4","5","6","7","8","9"]
def display():
    print(" --- --- --- ")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print(" --- --- --- ")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print(" --- --- --- ")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print(" --- --- --- ")

def turn():
    display()
    while True:
        pos = int(input("Choose The Vacant Position: "))
        if board[pos-1] != "X" and  board[pos-1] != "O":
                board[pos-1] = playersym
                display()
                return board
        else:
            print("Invalid Move!")
            display()
            continue

import random
def ai():
    while True:
        pos = random.randint(1,9)
        if board[pos-1] != "X" and  board[pos-1] != "O":
                board[pos-1] = aisym
                return board

def chk_win():
    win_combo = [[0,1,2],[0,4,8],[0,3,6],[2,4,6],[2,5,8],[6,7,8],[3,4,5],[1,4,7]]
    for combo in win_combo:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            print(f"{turnsym} won!")
            return True
    return False

mode = input("Continue with training mode<y/n>?")
if mode != "y":
    print("AI will play with [X or O]?: ")
    aisym = input("")
    if aisym == "O":
        playersym = "X"
    else:
        playersym = "O"

    print("Who will play first?:")
    print("1. You")
    print("2. AI")
    turn_choice = int(input(""))
    if turn_choice == 1:
        turn1 = True
    else:
        turn2 = False

    for i in range(9):
        while turn1:
            print(f"{playersym} turn")
            turnsym = playersym
            board = turn()
            turn1 = False
            turn2 = True
        win = chk_win()
        if win:
            break
        while turn2:
            print(f"{aisym} turn")
            turnsym = aisym
            board = ai()
            display()
            win = chk_win()
            turn1 = True
            turn2 = False
        win = chk_win()
        if win:
            break
else:
    sym1 = "O"
    sym2 = "X"
    turn1 = True
    for i in range(9):
        while turn1:
            aisym = sym1
            turnsym = aisym
            board = ai()
            turn1 = False
            turn2 = True
        win = chk_win()
        if win:
            break
        while turn2:
            aisym = sym2
            turnsym = aisym
            board = ai()
            win = chk_win()
            turn1 = True
            turn2 = False
        win = chk_win()
        if win:
            break