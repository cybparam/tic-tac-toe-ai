import time
import random
import json

try:
    with open("training_data.json", "r") as file:
        memory = json.load(file)
    for state in memory:
        memory[state] = {int(pos): score for pos, score in memory[state].items()}
except FileNotFoundError:
    memory = {}

def get_state():
    return "".join(board)

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

def ai():
    global memory

    avlpos = []
    for i in range(0,9):
        if board[i] != "X" and board[i] != "O":
            avlpos.append(i)
    
    state = get_state()
    if state in memory:
        if mode != "y":
            best_pos = max(avlpos, key=lambda pos: memory[state].get(pos, 0))
            pos = best_pos
        else:
            if random.random() < 0.2:
                pos = random.choice(avlpos)
            else:
                best_pos = max(avlpos, key=lambda pos: memory[state].get(pos, 0))
                pos = best_pos
    else:
        pos = random.choice(avlpos)

    board[pos] = aisym
    if mode != "y":
        return board, pos
    else:
        return board, pos, state

def upd_memory():
    global memory

    if state not in memory:
        memory[state] = {}
    if pos not in memory[state]:
        memory[state][pos] = 0

    return memory

def learn(history, reward):
    for state, pos in history:
        memory[state][pos] += reward
    return memory

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
                    winner = "O"
                    wino += 1
                else:
                    winner = "X"
                    winx += 1
                return True, wino, winx, winner
            
    if mode != "y":
        return False
    else:
        wino, winx = wino, winx
        return False, wino, winx, ""

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

def force():
    global mode
    mode = "y"
    print("Forced to training mode!")
    return mode

while True:
    mode = input("Continue with training mode <y/n> ?: ")

    if mode != "y":
        mode2 = input("Continue with testing <y/n> ?: ")
        if mode2 != "y":
            break
        else:
            print("Starting Testing Mode... ")
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
            brk = input("Wanna Exit The Game <y/n> ?: ")
            if brk == "y":
                break
    else:
        games = int(input("Enter Number of games: "))
        winx, wino, drawc = 0, 0, 0

        for i in range(games):
            xhistory = []
            ohistory = []

            if random.random() < 0.5:
                turn1 = True
            else:
                turn2, turn1 = True, False
            move = 0

            while True:
                while turn1:
                    aisym = "O"
                    turnsym = aisym
                    board, pos, state = ai()
                    ohistory.append((state, pos))
                    memory = upd_memory()
                    turn1, turn2 = False, True
                    
                win, wino, winx, winner = chk_win()

                if not win:
                    move += 1
                    draw, drawc = chk_draw()
                if draw:
                    winner = "draw"
                if win or draw:
                    board = reset()
                    break

                while turn2:
                    aisym = "X"
                    turnsym = aisym
                    board, pos, state = ai()
                    xhistory.append((state, pos))
                    memory = upd_memory()
                    turn1, turn2 = True, False

                win, wino, winx, winner = chk_win()

                if not win:
                    move += 1
                    draw, drawc = chk_draw()
                if draw:
                    winner = "draw"
                if win or draw:
                    board = reset()
                    break

            if winner == "O":
                memory = learn(ohistory, 1)
                memory = learn(xhistory, -1)
            elif winner == "X":
                memory = learn(xhistory, 1)
                memory = learn(ohistory, -1)
            else:
                memory = learn(ohistory, 0)
                memory = learn(xhistory, 0)

        print(f"O won {wino} Times, X won {winx} Times, There were {drawc} Draws")

with open("training_data.json", "w") as file:
    json.dump(memory, file, indent=4)