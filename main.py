spieler1 = "X"
spieler2 = "O"
currentTurn = 1
brett = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def printBrett():
    for i in range(3):
        print(brett[i][0] + " | " + brett[i][1] + " | " + brett[i][2])
        if i < 2:
            print("---------")
printBrett()

def isFree(reihe, spalte):
    if brett[reihe][spalte] == " ":
        return True
    else:
        return False

def whichSpieler():
    return spieler1 if currentTurn == 1 else spieler2

def convNumToField(num):
    return num;

def place(reihe, spalte):
    if isFree(reihe, spalte):
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

    if isRow and isLine and isDiagonal:
        return True
    else:
        return False

def checkDraw():
    isDraw = True
    for i in range(3):
        for j in range(3):
            if type(brett[i][j]) == int:
                isDraw = False
    return isDraw

def startGame():
    print("Spiel geht los!\n")
    printBrett()
