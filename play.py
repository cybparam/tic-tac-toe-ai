import time
import random
import json

with open("training_data.json", "r") as file:
    memory = json.load(file)
for state in memory:
    memory[state] = {int(pos): score for pos, score in memory[state].items()}

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

def get_state():
    return "".join(board)

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

def ai():
    global memory

    avlpos = []
    for i in range(0,9):
        if board[i] != "X" and board[i] != "O":
            avlpos.append(i)
    
    state = get_state()
    if state in memory:
        best_pos = max(avlpos, key=lambda pos: memory[state].get(pos, 0))
        pos = best_pos

    else:
        pos = random.choice(avlpos)

    board[pos] = aisym
    return board, pos

def chk_win():
    win_combo = [[0,1,2],[0,4,8],[0,3,6],[2,4,6],[2,5,8],[6,7,8],[3,4,5],[1,4,7]]

    for combo in win_combo:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
                print(f"{turnsym} won!")
                return True
    return False

def chk_draw():
    if move == 9:
        return True
    else:
        return False

while True:
    print("Starting Game... ")

    for i in range(1,4):
        time.sleep(1)
        print(i)

    move = 0
    aisym = input("Choose a symbol for ai [X or O]: ")
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
        turn1, turn2 = False, True

    while True:
        while turn1:
            print(f"{playersym} turn")
            turnsym = playersym
            board = turn()
            turn1, turn2 = False, True
        win = chk_win()
        if not win:
            move += 1
            draw = chk_draw()
        if win or draw:
            display()
            if draw:
                print("Draw!")
            board = reset()
            break
        while turn2:
            print(f"{aisym} turn")
            turnsym = aisym
            board, _ = ai()
            display()
            turn1, turn2 = True, False
        win = chk_win()
        if not win:
            move += 1
            draw = chk_draw()
        if win or draw:
            display()
            if draw:
                print("Draw!")
            board = reset()
            break
    brk = input("Continue The Game <y/n> ?: ")
    if brk != "y":
        break