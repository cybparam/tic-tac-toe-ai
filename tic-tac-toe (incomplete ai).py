import time

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

def reset():
    board = ["1","2","3","4","5","6","7","8","9"]
    return board

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
        pos = pos - 1
        if board[pos] != "X" and  board[pos] != "O":
                board[pos] = aisym
                return board, pos

def monitor():
    display()
    print(f"Played {turnsym} at {pos}")
    time.sleep(2)

def chk_win():
    global wino, winx
    win_combo = [[0,1,2],[0,4,8],[0,3,6],[2,4,6],[2,5,8],[6,7,8],[3,4,5],[1,4,7]]
    for combo in win_combo:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            if mode != "y":
                print(f"{turnsym} won!")
                return True
            else:
                if turnsym == "O":
                    wino += 1
                else:
                    winx += 1
                return True, wino, winx
            
    if mode != "y":
        return False
    else:
        wino, winx = wino, winx
        return False, wino, winx

def chk_draw():
    global drawc
    if move == 9:
        if mode != "y":
            return True
        else:
            drawc += 1
            return True, drawc
    else:
        if mode != "y":
            return False
        else:
            drawc = drawc
            return False, drawc

mode = input("Continue with training mode<y/n>?")
if mode != "y":
    move = 0
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
        turn1 = False

    while True:
        move += 1
        while turn1:
            print(f"{playersym} turn")
            turnsym = playersym
            board = turn()
            turn1 = False
            turn2 = True
        win = chk_win()
        draw = chk_draw()
        if win or draw:
            break
        move += 1
        while turn2:
            print(f"{aisym} turn")
            turnsym = aisym
            board, _ = ai()
            display()
            turn1 = True
            turn2 = False
        win = chk_win()
        draw = chk_draw()
        if win or draw:
            break
else:
    games = int(input("Enter Number of games: "))
    winx, wino, drawc = 0, 0, 0
    for i in range(games):
        move = 0
        sym1 = "O"
        sym2 = "X"
        turn1 = True
        while True:
            while turn1:
                aisym = sym1
                turnsym = aisym
                board, pos = ai()
                turn1 = False
                turn2 = True
            win, wino, winx = chk_win()
            move += 1
            draw, drawc = chk_draw()
            if win or draw:
                board = reset()
                break
            while turn2:
                aisym = sym2
                turnsym = aisym
                board, pos = ai()
                turn1 = True
                turn2 = False
            win, wino, winx = chk_win()
            move += 1
            draw, drawc = chk_draw()
            if win or draw:
                board = reset()
                break
    print(f"O won {wino} Times, X won {winx} Times, There were {drawc} Draws")