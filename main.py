spieler1 = "X"
spieler2 = "O"
currentTurn = "1"
gameRuns = False
brett = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def printBrett():
    for i in range(3):
        print(brett[i][0] + " | " + brett[i][1] + " | " + brett[i][2])
        if i < 2:
            print("---------")
printBrett()

def isFree(reihe, spalte):
    if brett[reihe][spalte] in ["X", "O"]:
        return False
    else:
        return True

def whichSpieler():
    return spieler1 if currentTurn == "1" else spieler2

def convNumToField(num):
    if num == 1 :
        return [0, 0]
    elif num == 2:
        return [0, 1]
    elif num == 3:
        return [0, 2]
    elif num == 4:
        return [1, 0]
    elif num == 5:
        return [1, 1]
    elif num == 6:
        return [1, 2]
    elif num == 7:
        return [2, 0]
    elif num == 8:
        return [2, 1]
    else:
        return [2, 2]

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

    if isRow or isLine or isDiagonal:
        return True
    else:
        return False

def startGame():
    global currentTurn
    gameRuns = True
    print("Spiel geht los!\n")
    printBrett()
    while(gameRuns):
        chosenField = int(input("Spieler " + currentTurn + ", wähle dein Feld: "))
        while(True):
            chosenRow = (convNumToField(chosenField))[0]
            chosenLine = convNumToField(chosenField)[1]
            if not isFree(chosenRow, chosenLine):
                chosenField = int(input("Ein freies Feld bitte: "))
            else:
                place(chosenRow, chosenLine)
                printBrett()
                break
        if checkWin():
            print("Spieler " + currentTurn + " hat gewonnen!")
            gameRuns = False
        else:
            currentTurn = "2" if currentTurn == "1" else "1"

while True:
    brett = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    startGame()
    print("\n" * 8)

