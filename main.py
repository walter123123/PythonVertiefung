spieler1 = "X"
spieler2 = "O"
currentTurn = "1"
punktestand = [0, 0]
gameRuns = False
brett = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def printBrett():
    for i in range(3):
        print(brett[i][0] + " | " + brett[i][1] + " | " + brett[i][2])
        if i < 2:
            print("---------")

def isFree(reihe, spalte):
    return brett[reihe][spalte] not in ["X", "O"]

def whichSpieler():
    return spieler1 if currentTurn == "1" else spieler2

def convNumToField(num):
    row = int((num - 1) / 3)
    line = (num - 1) % 3
    return [row, line]

def place(reihe, spalte):
    brett[reihe][spalte] = whichSpieler()

def checkWin():
    isRow = False
    isLine = False
    isDiagonal = False
    for i in range(3):
        if brett[i][0] == brett[i][1] == brett[i][2] == whichSpieler():
            isRow = True
    for i in range(3):
        if brett[0][i] == brett[1][i] == brett[2][i] == whichSpieler():
            isLine = True
    if brett[0][0] == brett [1][1] == brett[2][2] == whichSpieler():
        isDiagonal = True
    elif brett[0][2] == brett[1][1] == brett[2][0] == whichSpieler():
        isDiagonal = True

    return isRow or isLine or isDiagonal

def checkDraw():
    for i in range(3):
        for j in range(3):
            if brett[i][j] not in ["X", "O"]:
                return False
    return True

def numIsOK(num):
    if not num.isdigit():
        return False
    num = int(num)
    if num not in range(1, 10):
        return False
    chosenRow = convNumToField(num)[0]
    chosenLine = convNumToField(num)[1]
    if not isFree(chosenRow, chosenLine):
        return False
    else:
        return True

def startGame():
    global currentTurn
    gameRuns = True
    print("Spiel geht los!\n")
    printBrett()
    while(gameRuns):
        chosenField = input("Spieler " + currentTurn + ", wähle dein Feld: ")
        while(not numIsOK(chosenField)):
            chosenField =input("bitte ein gültiges Feld: ")
        chosenField = int(chosenField)
        chosenRow = (convNumToField(chosenField))[0]
        chosenLine = convNumToField(chosenField)[1]
        place(chosenRow, chosenLine)
        print("\n" * 6)
        printBrett()

        if checkWin():
            print("Spieler " + currentTurn + " hat gewonnen!")
            punktestand[int(currentTurn) - 1] += 1
            gameRuns = False
        elif checkDraw():
            print("Unentschieden!")
            gameRuns = False
        else:
            currentTurn = "2" if currentTurn == "1" else "1"

while True:
    brett = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    print("Momentaner Punktestand:\nSpieler 1: " + str(punktestand[0]) + "\nSpieler 2: " + str(punktestand[1]))
    startGame()
    print("\n" * 2)
    input("Enter drücken für neues Spiel")
    print("\n" * 8)

