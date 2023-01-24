# // IMPORTING // #
import replit
import random


# // FUNCTIONS // #

# Board Setup
def setupBoard():
    # Creates a temporary array and creates 2 houses from the first era and makes the rest empty, then returns the board
    setup = []
    setup.append(["A", 0])
    setup.append(["A", 0])
    for i in range(43):
        setup.append(["-", 0])
    return setup


# Time Rules
def timeChange(time):
    # Ancient Era 4000 BCE - 500 BCE
    # Classical Era 499 BCE - 800 AD
    # Medieval Era 801 AD - 1399 AD
    # Renaissance Era 1400 AD - 1799 AD
    # Industrial Era 1800 AD - 1899 AD
    # Modern Era 1900 AD - 1945 AD
    # Atomic Era 1946 AD - 1991 AD
    # Information Era 1992 AD - 2200 AD
    # Age of Dawn 2200+ AD

    # 60 years: 4000 --> 1000
    # 40 years: 1000 --> 200 AD
    # 30 years: 200 --> 800
    # 20 years: 800 --> 1400
    # 10 years: 1400 --> 1650
    # 5 years: 1650 --> 1850
    # 2 years: 1850 --> 1980
    # 1 year: 1980 --> 2200

    # Creates temporary variables for the time, increments turn by 1
    newTurn = time[0] + 1
    newYear = time[1]
    newCalender = time[2]
    newEra = time[3]
    newEraNumber = time[4]

    # Finds whether it is BCE or AD based off the year
    if time[2] == "BCE":
        if time[1] > 1000:
            newYear -= 500
        elif time[1] > 0:
            newYear -= 250

    elif time[2] == "":
        newYear += 250
        newCalender = "AD"

    elif time[2] == "AD":
        if time[1] < 200:
            newYear += 250
        elif time[1] < 800:
            newYear += 40
        elif time[1] < 1400:
            newYear += 20
        elif time[1] < 1650:
            newYear += 10
        elif time[1] < 1850:
            newYear += 5
        elif time[1] < 1980:
            newYear += 2
        elif time[1] >= 1980:
            newYear += 1

    if newYear == 0:
        newCalender = ""

    # Determines the Era and Era Number it is in based off the year and BCE/AD
    if newCalender == "BCE":
        if newYear <= 4000 and newYear >= 500:
            newEra = "Ancient Era"
            newEraNumber = 0
        elif newYear <= 499:
            newEra = "Classical Era"
            newEraNumber = 1

    elif newCalender == "AD":
        if newYear <= 800:
            newEra = "Classical Era"
            newEraNumber = 1
        elif newYear <= 1399:
            newEra = "Medieval Era"
            newEraNumber = 2
        elif newYear <= 1799:
            newEra = "Renaissance Era"
            newEraNumber = 3
        elif newYear <= 1899:
            newEra = "Industrial Era"
            newEraNumber = 4
        elif newYear <= 1945:
            newEra = "Modern Era"
            newEraNumber = 5
        elif newYear <= 1991:
            newEra = "Atomic Era"
            newEraNumber = 6
        elif newYear <= 2200:
            newEra = "Information Era"
            newEraNumber = 7
        elif newYear > 2200:
            newEra = "Age of Dawn"
            newEraNumber = 7

    return [newTurn, newYear, newCalender, newEra, newEraNumber]


# Print Board
def printBoard(board):
    for k in range(5):
        for i in range(9):
            print(str(board[9 * k + i][0]) + " ", end=" ")
        print("\n")


# Tutorial
def tutorial():
    print("_________________________________________________________")
    print("                                                         ")
    print("                || A   N E W   D A W N ||                ")
    print("_________________________________________________________")
    print("                                                         ")
    print(" A New Dawn is a turn-based civilization simulator where ")
    print("the player controls a nation. With this power, the player")
    print("gathers resources to create buildings, builds an army to ")
    print("  defend and attack, and make decisions on national and  ")
    print("                     foreign policy.                     ")
    print("                                                         ")
    input("                 Press enter to continue                 ")
    print("                                                         ")
    print("_________________________________________________________")
    print("                                                         ")
    print("                                                         ")
    print("                -  -  -  -  -  -  -  -  -                ")
    print("                -  -  -  -  -  -  -  -  -                ")
    print("                -  -  -  -  -  -  -  -  -                ")
    print("                -  -  -  -  -  -  -  -  -                ")
    print("                -  -  -  -  -  -  -  -  -                ")
    print("                                                         ")
    print("This is an empty board where you will place buildings on.")
    print("  The hyphen (-) represents an empty, buildable, plot.   ")
    print("                                                         ")
    input("                 Press enter to continue                 ")
    print("                                                         ")
    print("_________________________________________________________")
    print("                                                         ")
    print("                                                         ")
    print("                -  -  -  -  -  -  -  -  -                ")
    print("                -  -  -  -  -  -  -  -  -                ")
    print("                -  -  -  -  -  -  -  -  -                ")
    print("                -  -  -  -  -  -  -  -  -                ")
    print("                -  -  -  -  -  -  -  -  -                ")
    print("                                                         ")
    print(" Each position on the board is represented by a number.  ")
    print(" The value of the position is determined by the row and  ")
    print(" column with the equation column + ((row - 1) * 9). For  ")
    print("  example the value at column 3 and row 3 would be 21.   ")
    print("                                                         ")
    input("                 Press enter to continue                 ")
    print("                                                         ")
    print("_________________________________________________________")
    print("                                                         ")
    print("                                                         ")
    print("  On the board, each symbol represents a building type.  ")
    print("                    Ex: H = Hospital.                    ")
    print("                                                         ")
    print("  The amount of resources you have and other important   ")
    print("             will be shown under the board.              ")
    print("                                                         ")
    input("                 Press enter to continue                 ")
    print("                                                         ")
    print("_________________________________________________________")
    print("                                                         ")
    print("                                                         ")
    print(" Whenever a new event occurs, it will inform you at the  ")
    print("   bottom of the page and await your response. As you    ")
    print("    progress through the eras, more events will occur    ")
    print("                                                         ")
    print("In addition, you will unlock new resources and buildings.")
    print("                                                         ")
    print("  All old buildings will not get upgraded immediately.   ")
    print("                                                         ")
    input("                 Press enter to continue                 ")
    print("                                                         ")
    print("_________________________________________________________")
    print("                                                         ")
    print("                                                         ")
    print("  You can lose the game if your population hits 0 or if  ")
    print("              another nation occupies you.               ")
    print("                                                         ")
    input("                 Press enter to continue                 ")
    print("                                                         ")
    print("_________________________________________________________")
    print("                                                         ")
    print("                                                         ")
    print("As you progress further into the game, you will reach the")
    print("Age of Dawn where you face a world threatening event. If ")
    print("you survive or escape, you will have completed the game. ")
    print("                                                         ")
    input("                 Press enter to continue                 ")
    print("                                                         ")
    print("_________________________________________________________")
    print("                                                         ")
    print("                                                         ")
    print("               // Building Information //                ")
    print("                                                         ")
    print("Hospital/Personal Care (H): decreases the mortality rate.")
    print("    0% -> 2% -> 5% -> 10% -> 20% -> 50% -> 75% -> 90%    ")
    print("                                                         ")
    print("  Yurt/Small House/House/Large House/Mansion/Apartment   ")
    print("      Capsule Apartment (A): increases population.       ")
    print("    1 -> 2 -> 7 -> 12 -> 25 -> 2500 -> 5000 -> 100000    ")
    print("                                                         ")
    print(" Farm/Planation/Farming Estate/Factory Farms/Greenhouse  ")
    print("GMO Automation Greenhouse and Fishing Farm (P): increases")
    print("                          food.                          ")
    print("2 -> 5 -> 25 -> 50 -> 2500 -> 10000 -> 25000 -> 999999999")
    print("                                                         ")
    print("Blacksmith/Gunsmith/Army Camp/Weapons Factory/War Machine")
    print("        Factory (W): increases military strength         ")
    print("   0 -> 2 -> 5 -> 25 -> 250 -> 500 -> 10000 -> 1000000   ")
    print("                                                         ")
    print("            Lumbermill (L): produces 10 wood             ")
    print("                                                         ")
    print("        Quarry (S): produces 5 stone and 1 metal         ")
    print("                                                         ")
    print("  Factory/Semi-Automated Factory/Automated Factory (F):  ")
    print("             produces all relevant resources             ")
    print("               Wood: 200 -> 2000 -> 0 -> 0               ")
    print("               Stone: 100 -> 1000 -> 0 -> 0              ")
    print("             Metal: 10 -> 100 -> 1000-> 10000            ")
    print("            Steel: 5 -> 100 -> 2000 -> 1000000           ")
    print("           Cement: 0 -> 10 -> 200 -> 10000000            ")
    print("            Aluminum: 0 -> 0 -> 100 -> 100000            ")
    print("             Titanium: 0 -> 0 -> 10 -> 1000              ")
    print("               Uranium: 0 -> 0 -> 5 -> 100               ")
    print("                                                         ")
    input("                 Press enter to continue                 ")
    print("                                                         ")
    print("_________________________________________________________")
    print("                                                         ")
    print("                                                         ")
    print("                       // Tips //                        ")
    print("                                                         ")
    print("          Only build 1 hospital or Personal Care         ")
    print("     Increase your population to increase your gold      ")
    print("  Make sure your population is supported by enough food  ")
    print("  Trading and helping countries improves your relations  ")
    print("                                                         ")
    input("                   Press enter to exit                   ")
    print("                                                         ")
    print("_________________________________________________________")


# Start Menu
def start():
    print("_________________________")
    print("                         ")
    print("|| A   N E W   D A W N ||")
    print("_________________________")
    print("                         ")
    print("      by xilacxilac      ")
    print("                         ")
    print("                         ")
    print("          Play           ")
    print("                         ")
    print("        Tutorial         ")
    print("                         ")
    print("          Exit           ")
    print("                         ")
    print("                         ")


# Determines if the player lost the game or not
def lostGame(pop):
    # Lost if population is 0
    if pop == 0:
        return True

    return False


# Finds the maximum population the player can have with their current buildings
def maxPop(housing):
    # Numbers Setup
    house = [1, 2, 7, 12, 25, 2500, 5000, 100000]
    maxpop = 0

    for i in range(8):
        maxpop += (house[i] * housing[i])

    return maxpop


# Determines the change in resources per turn from production to death
def resourcesChange(resources, buildings, eraNumber, maxpop, disease, war, percent):
    # Numbers Setup
    hospital = [0, 2, 5, 10, 20, 50, 75, 99]
    house = [1, 2, 7, 12, 25, 2500, 5000, 100000]
    farm = [2, 5, 25, 50, 2500, 10000, 25000, 999999999]
    weapons = [0, 2, 5, 25, 250, 500, 10000, 1000000]
    lumbermill = [0, 10, 10, 10, 10, 10, 10, 10]
    quarryStone = [0, 5, 5, 5, 5, 5, 5, 5]
    quarryMetal = [0, 1, 1, 1, 1, 1, 1, 1]
    factoryWood = [0, 0, 0, 0, 200, 2000, 0, 0]
    factoryStone = [0, 0, 0, 0, 100, 1000, 0, 0]
    factoryMetal = [0, 0, 0, 0, 10, 100, 1000, 10000]
    factorySteel = [0, 0, 0, 0, 5, 100, 2000, 1000000]
    factoryCement = [0, 0, 0, 0, 0, 10, 200, 10000000]
    factoryAluminum = [0, 0, 0, 0, 0, 0, 100, 100000]
    factoryTitanium = [0, 0, 0, 0, 0, 0, 10, 1000]
    factoryUranium = [0, 0, 0, 0, 0, 0, 5, 100]

    # New Values
    # resources = [wood, stone, metal, steel, cement, aluminum, titanium, uranium, population, food, strength, gold]
    newResources = []
    for i in range(len(resources)):
        newResources.append(resources[i])

    newResources[0] += (lumbermill[eraNumber] * buildings[5])
    newResources[1] += (quarryStone[eraNumber] * buildings[4])
    newResources[2] += (quarryMetal[eraNumber] * buildings[4])

    # Gold
    newResources[11] += (eraNumber * resources[8])

    # Sets new resources
    for i in range(len(resources)):
        for j in range(8):
            if i == 0:
                # Wood
                newResources[0] += (factoryWood[j] * buildings[6][j])
            elif i == 1:
                # Stone
                newResources[1] += (factoryStone[j] * buildings[6][j])
            elif i == 2:
                # Metal
                newResources[2] += (factoryMetal[j] * buildings[6][j])
            elif i == 3:
                # Steel
                newResources[3] += (factorySteel[j] * buildings[6][j])
            elif i == 4:
                # Cement
                newResources[4] += (factoryCement[j] * buildings[6][j])
            elif i == 5:
                # Aluminum
                newResources[5] += (factoryAluminum[j] * buildings[6][j])
            elif i == 6:
                # Titanium
                newResources[6] += (factoryTitanium[j] * buildings[6][j])
            elif i == 7:
                # Uranium
                newResources[7] += (factoryUranium[j] * buildings[6][j])
            elif i == 9:
                # Food
                newResources[9] += (farm[j] * buildings[2][j])
            elif i == 10:
                # Strength
                newResources[10] += (weapons[j] * buildings[3][j])

    # Population
    newResources[8] = pop(disease, war, resources[9], resources[8], hospital, maxpop, buildings[0], percent)

    # Food
    newResources[9] -= resources[8]

    if eraNumber == 0:
        newResources[0] += (16 * newResources[8])
        newResources[1] += (8 * newResources[8])

    if newResources[9] < 0:
        newResources[9] = 0

    return newResources


# Called by resourceChange() to determine the new population based off maximum population, food, disease/war, etc.
def pop(disease, war, food, pop, hospital, maxpop, building, percent):
    value = -1
    for i in building:
        if building[i] > 0:
            value = i

    newPop = dead(pop, disease, war, hospital, value, percent)

    if newPop > food and food != 0:
        return newPop - food

    elif food == 0:
        return 0

    elif round(newPop * 1.5) <= maxpop:
        return round(newPop * 1.5)

    else:
        return maxpop


# Called by pop() to find how many people die by disease and war, and how many survive based off hospital levels
def dead(pop, disease, war, hospital, value, percent):
    newPop = pop
    if disease == False and war == False:
        newPop = pop

    elif disease == True and war == False:
        if value != -1:
            newPop = round(pop * 9 / 10) + round((hospital[value] / 100) * (pop / 10))

    elif disease == False and war == True:
        newPop = ((100 - percent) / 100) * pop

    else:
        if value != -1:
            newPop = round(pop * 9 / 10) + round((hospital[value] / 100) * (pop / 10))
        newPop = ((100 - percent) / 100) * newPop

    return newPop


# Prints the current resources the player has
def printResources(resources, maxpop, buildings, eraNumber, disease):
    resourceTurn = resourcesChange(resources, buildings, eraNumber, maxpop, disease, False, 0)
    for i in range(len(resourceTurn)):
        resourceTurn[i] = resourceTurn[i] - resources[i]

    signPop = "+"
    if resourceTurn[8] < 0:
        signPop = ""

    signFood = "+"
    if resourceTurn[9] < 0:
        signFood = ""

    print("\nGold: " + str(resources[11]) + " (+" + str(resourceTurn[11]) + ")")
    print("Population: " + str(resources[8]) + " (" + signPop + str(resourceTurn[8]) + ") / " + str(maxpop))
    print("Food: " + str(resources[9]) + " (" + signFood + str(resourceTurn[9]) + ")")
    print("Military Strength: " + str(resources[10]) + " (+" + str(resourceTurn[10]) + ")")
    print("")
    print("Wood: " + str(resources[0]) + " (+" + str(resourceTurn[0]) + ")")
    print("Stone: " + str(resources[1]) + " (+" + str(resourceTurn[1]) + ")")
    print("Metal: " + str(resources[2]) + " (+" + str(resourceTurn[2]) + ")")
    print("Steel: " + str(resources[3]) + " (+" + str(resourceTurn[3]) + ")")
    print("Cement: " + str(resources[4]) + " (+" + str(resourceTurn[4]) + ")")
    print("Aluminum: " + str(resources[5]) + " (+" + str(resourceTurn[5]) + ")")
    print("Titanium: " + str(resources[6]) + " (+" + str(resourceTurn[6]) + ")")
    print("Uranium: " + str(resources[7]) + " (+" + str(resourceTurn[7]) + ")")


# Prints the current turn, time, and era name
def printTime(time):
    print("Turn: " + str(time[0]) + ", " + str(time[1]) + " " + time[2] + ", The " + time[3] + "\n")


# Calls printTime(), printBoard(), and printResources() along with replit.clear() in order to give a full print of all information
def fullPrint(time, resources, board, maxpop, buildings, eraNumber, disease, war, percent):
    replit.clear()
    printTime(time)
    printBoard(board)
    printResources(resources, maxpop, buildings, eraNumber, disease)


# Assigns the cost of each building for each time period
def buildingCost():
    # [wood, stone, metal, steel, cement, aluminum, titanium, uranium]
    h0 = [-1, -1, -1, -1, -1, -1, -1, -1]  # wood stone
    h1 = [150, 20, 0, 0, 0, 0, 0, 0]  # wood stone
    h2 = [200, 50, 1, 0, 0, 0, 0, 0]  # wood stone metal
    h3 = [200, 200, 5, 0, 0, 0, 0, 0]  # wood stone metal
    h4 = [500, 200, 20, 0, 0, 0, 0, 0]  # wood stone steel
    h5 = [2500, 1000, 50, 500, 0, 0, 0, 0]  # wood stone steel cement
    h6 = [0, 0, 0, 1000, 500, 50, 5, 1]  # aluminum titanium uranium
    h7 = [0, 0, 0, 10000000, 1000000, 10000, 1000, 100]  # aluminum titanium uranium
    h = []
    h.append(h0)
    h.append(h1)
    h.append(h2)
    h.append(h3)
    h.append(h4)
    h.append(h5)
    h.append(h6)
    h.append(h7)

    a0 = [150, 20, 0, 0, 0, 0, 0, 0]
    a1 = [200, 50, 0, 0, 0, 0, 0, 0]
    a2 = [300, 100, 5, 0, 0, 0, 0, 0]
    a3 = [300, 300, 10, 0, 0, 0, 0, 0]
    a4 = [1000, 400, 25, 20, 0, 0, 0, 0]
    a5 = [5000, 2500, 50, 500, 0, 0, 0, 0]
    a6 = [0, 0, 0, 1000, 1000, 100, 10, 0]
    a7 = [0, 0, 0, 1000000, 1000000, 10000, 1000, 100]
    a = []
    a.append(a0)
    a.append(a1)
    a.append(a2)
    a.append(a3)
    a.append(a4)
    a.append(a5)
    a.append(a6)
    a.append(a7)
    p0 = [50, 10, 0, 0, 0, 0, 0, 0]
    p1 = [75, 15, 0, 0, 0, 0, 0, 0]
    p2 = [150, 30, 0, 0, 0, 0, 0, 0]
    p3 = [300, 75, 5, 0, 0, 0, 0, 0]
    p4 = [500, 150, 20, 5, 0, 0, 0, 0]
    p5 = [2000, 500, 45, 100, 0, 0, 0, 0]
    p6 = [0, 0, 0, 100, 10000, 100, 10, 1]
    p7 = [0, 0, 0, 10000, 1000000, 10000, 1000, 100]
    p = []
    p.append(p0)
    p.append(p1)
    p.append(p2)
    p.append(p3)
    p.append(p4)
    p.append(p5)
    p.append(p6)
    p.append(p7)

    w0 = [-1, -1, -1, -1, -1, -1, -1, -1]
    w1 = [100, 100, 0, 0, 0, 0, 0, 0]
    w2 = [200, 200, 10, 0, 0, 0, 0, 0]
    w3 = [400, 400, 25, 0, 0, 0, 0, 0]
    w4 = [800, 800, 100, 10, 10, 0, 0, 0]
    w5 = [3200, 3200, 500, 500, 100, 0, 0, 0]
    w6 = [0, 0, 0, 1000, 100000, 1000, 100, 100]
    w7 = [0, 0, 0, 10000, 1000000, 10000, 1000, 1000]
    w = []
    w.append(w0)
    w.append(w1)
    w.append(w2)
    w.append(w3)
    w.append(w4)
    w.append(w5)
    w.append(w6)
    w.append(w7)

    f0 = [-1, -1, -1, -1, -1, -1, -1, -1]
    f1 = [-1, -1, -1, -1, -1, -1, -1, -1]
    f2 = [-1, -1, -1, -1, -1, -1, -1, -1]
    f3 = [-1, -1, -1, -1, -1, -1, -1, -1]
    f4 = [800, 800, 100, 10, 10, 0, 0, 0]
    f5 = [3200, 3200, 500, 500, 100, 0, 0, 0]
    f6 = [0, 0, 0, 10000, 100000, 1000, 100, 100]
    f7 = [0, 0, 0, 100000, 1000000, 10000, 1000, 1000]
    f = []
    f.append(f0)
    f.append(f1)
    f.append(f2)
    f.append(f3)
    f.append(f4)
    f.append(f5)
    f.append(f6)
    f.append(f7)

    s0 = [-1, -1, -1, -1, -1, -1, -1, -1]
    s1 = [75, 15, 0, 0, 0, 0, 0, 0]
    s = []
    s.append(s0)
    s.append(s1)

    l0 = [-1, -1, -1, -1, -1, -1, -1, -1]
    l1 = [75, 15, 0, 0, 0, 0, 0, 0]
    l = []
    l.append(l0)
    l.append(l1)

    full = []
    full.append(h)
    full.append(a)
    full.append(p)
    full.append(w)
    full.append(f)
    full.append(s)
    full.append(l)
    return full


# Counts the amount of each building based off the current board state
def countBuilding(board):
    # Setup
    buildings = []
    buildings.append([0, 0, 0, 0, 0, 0, 0, 0])  # H
    buildings.append([0, 0, 0, 0, 0, 0, 0, 0])  # A
    buildings.append([0, 0, 0, 0, 0, 0, 0, 0])  # P
    buildings.append([0, 0, 0, 0, 0, 0, 0, 0])  # W
    buildings.append(0)  # S
    buildings.append(0)  # L
    buildings.append([0, 0, 0, 0, 0, 0, 0, 0])  # F

    for plot in board:
        if plot[0] == "H":
            buildings[0][plot[1]] += 1
        elif plot[0] == "A":
            buildings[1][plot[1]] += 1
        elif plot[0] == "P":
            buildings[2][plot[1]] += 1
        elif plot[0] == "W":
            buildings[3][plot[1]] += 1
        elif plot[0] == "S":
            buildings[4] += 1
        elif plot[0] == "L":
            buildings[5] += 1
        elif plot[0] == "F":
            buildings[6][plot[1]] += 1

    return buildings


# Prints the cost to build each building
def printBuildingCost(resourcesCost):
    for i in range(len(resourcesCost)):
        if resourcesCost[i] == -1:
            break
        elif resourcesCost[i] == 0:
            break
        elif i == 0:
            print(str(resourcesCost[i]) + " wood")
        elif i == 1:
            print(str(resourcesCost[i]) + " stone")
        elif i == 2:
            print(str(resourcesCost[i]) + " metal")
        elif i == 3:
            print(str(resourcesCost[i]) + " cement")
        elif i == 4:
            print(str(resourcesCost[i]) + " steel")
        elif i == 5:
            print(str(resourcesCost[i]) + " aluminum")
        elif i == 6:
            print(str(resourcesCost[i]) + " titanium")
        elif i == 7:
            print(str(resourcesCost[i]) + " uranium")
    print("")


# Prints the buyable buildings based off an era and returns the symbols of the buildings of the buyable buildings
def buyableBuilding(eraNumber):
    cost = buildingCost()

    # Ancient
    if eraNumber == 0:
        print("A: Yurt (Housing)")
        printBuildingCost(cost[1][eraNumber])
        print("P: Farm (Farming)")
        printBuildingCost(cost[2][eraNumber])
        return ["A", "P"]
    # Classical
    elif eraNumber == 1:
        print("H: Hospital (Medicine)")
        printBuildingCost(cost[0][eraNumber])
        print("A: Small House (Housing)")
        printBuildingCost(cost[1][eraNumber])
        print("P: Farm (Farming)")
        printBuildingCost(cost[2][eraNumber])
        print("W: Blacksmith (Weapons)")
        printBuildingCost(cost[3][eraNumber])
        print("S: Quarry (Mining)")
        printBuildingCost(cost[5][1])
        print("L: Lumbermill (Lumber)")
        printBuildingCost(cost[6][1])
        return ["H", "A", "P", "W", "S", "L"]
    # Medieval
    elif eraNumber == 2:
        print("H: Hospital (Medicine)")
        printBuildingCost(cost[0][eraNumber])
        print("A: House (Housing)")
        printBuildingCost(cost[1][eraNumber])
        print("P: Plantation (Farming)")
        printBuildingCost(cost[2][eraNumber])
        print("W: Blacksmith (Weapons)")
        printBuildingCost(cost[3][eraNumber])
        print("S: Quarry (Mining)")
        printBuildingCost(cost[5][1])
        print("L: Lumbermill (Lumber)")
        printBuildingCost(cost[6][1])
        return ["H", "A", "P", "W", "S", "L"]
    # Renaissance
    elif eraNumber == 3:
        print("H: Hospital (Medicine)")
        printBuildingCost(cost[0][eraNumber])
        print("A: Large House (Housing)")
        printBuildingCost(cost[1][eraNumber])
        print("P: Farming Estate (Farming)")
        printBuildingCost(cost[2][eraNumber])
        print("W: Gunsmith (Weapons)")
        printBuildingCost(cost[3][eraNumber])
        print("S: Quarry (Mining)")
        printBuildingCost(cost[5][1])
        print("L: Lumbermill (Lumber)")
        printBuildingCost(cost[6][1])
        return ["H", "A", "P", "W", "S", "L"]
    # Industrial
    elif eraNumber == 4:
        print("H: Hospital (Medicine)")
        printBuildingCost(cost[0][eraNumber])
        print("A: Mansion (Housing)")
        printBuildingCost(cost[1][eraNumber])
        print("P: Factory Farms (Farming)")
        printBuildingCost(cost[2][eraNumber])
        print("W: Army Camp (Weapons)")
        printBuildingCost(cost[3][eraNumber])
        print("F: Factory")
        printBuildingCost(cost[4][eraNumber])
        return ["H", "A", "P", "W", "F"]
    # Modern
    elif eraNumber == 5:
        print("H: Hospital (Medicine)")
        printBuildingCost(cost[0][eraNumber])
        print("A: Apartments (Housing)")
        printBuildingCost(cost[1][eraNumber])
        print("P: Factory Farms (Farming)")
        printBuildingCost(cost[2][eraNumber])
        print("W: Army Camp (Weapons)")
        printBuildingCost(cost[3][eraNumber])
        print("F: Factory")
        printBuildingCost(cost[4][eraNumber])
        return ["H", "A", "P", "W", "F"]
    # Atomic
    elif eraNumber == 6:
        print("H: Hospital (Medicine)")
        printBuildingCost(cost[0][eraNumber])
        print("A: Apartments (Housing)")
        printBuildingCost(cost[1][eraNumber])
        print("P: Greenhouse (Farming)")
        printBuildingCost(cost[2][eraNumber])
        print("W: Weapons Factory (Weapons)")
        printBuildingCost(cost[3][eraNumber])
        print("F: Semi-Automated Factory")
        printBuildingCost(cost[4][eraNumber])
        return ["H", "A", "P", "W", "F"]
    # Information
    elif eraNumber == 7:
        print("H: Personal Care (Medicine)")
        printBuildingCost(cost[0][eraNumber])
        print("A: Capsule Apartments (Housing)")
        printBuildingCost(cost[1][eraNumber])
        print("P: GMO Automation Greenhouse and Fishing Farm (Farming)")
        printBuildingCost(cost[2][eraNumber])
        print("W: War Machine Factory (Weapons)")
        printBuildingCost(cost[3][eraNumber])
        print("F: Automated Factory")
        printBuildingCost(cost[4][eraNumber])
        return ["H", "A", "P", "W", "F"]


# Called by changeGame() when the player wants to replace or buy a building; returns the new resources the player has after buying, a new board with the building on it, and a new array of buildings with the building added
def buy(board, resources, eraNumber, buildingType, index):
    cost = buildingCost()
    newBoard = []
    for i in range(len(board)):
        newBoard.append(board[i])

    newResources = []
    for i in range(len(resources)):
        newResources.append(resources[i])

    if buildingType == "H":
        if eraNumber == 0:
            print("ERROR: era building purchase failure")
            print("CAUSE: buy()")
            return [board, resources]
        else:
            resourceCost = cost[0][eraNumber]
    elif buildingType == "A":
        resourceCost = cost[1][eraNumber]
    elif buildingType == "P":
        resourceCost = cost[2][eraNumber]
    elif buildingType == "W":
        if eraNumber == 0:
            print("ERROR: era building purchase failure")
            print("CAUSE: buy()")
            return [board, resources]
        else:
            resourceCost = cost[3][eraNumber]
    elif buildingType == "S":
        if eraNumber >= 4 or eraNumber == 0:
            print("ERROR: era building purchase failure")
            print("CAUSE: buy()")
            return [board, resources]
        else:
            resourceCost = cost[5][1]
    elif buildingType == "L":
        if eraNumber >= 4 or eraNumber == 0:
            print("ERROR: era building purchase failure")
            print("CAUSE: buy()")
            return [board, resources]
        else:
            resourceCost = cost[6][1]
    elif buildingType == "F":
        if eraNumber < 4:
            print("ERROR: era building purchase failure")
            print("CAUSE: buy()")
            return [board, resources]
        else:
            resourceCost = cost[4][eraNumber]

    for i in range(len(resourceCost)):
        if resourceCost[i] == -1:
            print("Error: resource change failure")
            print("CAUSE: buy()")
            return [board, resources]
        else:
            if resources[i] < resourceCost[i]:
                print("Insufficient resources!")
                return [board, resources]
            else:
                newResources[i] -= resourceCost[i]

    print("\nPurchase successful!")
    newBoard[index] = [buildingType, eraNumber]
    return [newBoard, newResources]


# Tests if a variable is an integer or not
def isInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


# Allows the player to edit their buildings and get more information on them
def changeGame(board, resources, buidlings, eraNumber, maxpop, disease, war, percent):
    # Numbers Setup
    hospital = [0, 2, 5, 10, 20, 50, 75, 99]
    house = [1, 2, 7, 12, 25, 2500, 5000, 100000]
    farm = [2, 5, 25, 50, 2500, 10000, 25000, 999999999]
    weapons = [0, 2, 5, 25, 250, 500, 10000, 1000000]
    lumbermill = [0, 10, 10, 10, 10, 10, 10, 10]
    quarryStone = [0, 5, 5, 5, 5, 5, 5, 5]
    quarryMetal = [0, 1, 1, 1, 1, 1, 1, 1]
    factoryWood = [0, 0, 0, 0, 200, 2000, 0, 0]
    factoryStone = [0, 0, 0, 0, 100, 1000, 0, 0]
    factoryMetal = [0, 0, 0, 0, 10, 100, 1000, 10000]
    factorySteel = [0, 0, 0, 0, 5, 100, 2000, 1000000]
    factoryCement = [0, 0, 0, 0, 0, 10, 200, 10000000]
    factoryAluminum = [0, 0, 0, 0, 0, 0, 100, 100000]
    factoryTitanium = [0, 0, 0, 0, 0, 0, 10, 1000]
    factoryUranium = [0, 0, 0, 0, 0, 0, 5, 100]

    answer = input("\n\nInput end to finish your turn or anything else to continue: ")
    if answer == "end":
        return ["end"]

    fullPrint(time, resources, board, maxpop, buildings, eraNumber, disease, war, percent)
    plotNum = input("\n\nSelect a plot (1 - 45) or 0 to cancel: ")
    if not isInt(plotNum):
        plot = -1
    else:
        plot = int(plotNum)
    while plot < 0 or plot > 45 or not isInt(plotNum):
        fullPrint(time, resources, board, maxpop, buildings, eraNumber, disease, war, percent)
        plotNum = input("\n\nInvalid input, select a plot (1 - 45) or 0 to cancel: ")
        if not isInt(plotNum):
            plot = -1
        else:
            plot = int(plotNum)

    newBoard = []
    for i in range(len(board)):
        newBoard.append(board[i])
    newResources = []
    for j in range(len(resources)):
        newResources.append(resources[j])
    newBuildings = countBuilding(newBoard)

    if plot == 0:
        return [newBoard, newResources, newBuildings]

    if board[plot - 1][0] == "-":
        print("\nThe purchasable buildings are:")
        buyable = buyableBuilding(eraNumber)
        userBuilding = str(input("\nInput the symbol furthest to the left or cancel to cancel: ")).upper()
        while buyable.count(userBuilding) < 0 and userBuilding != "CANCEL":
            print("\n\nInvalid input, the purchasable buildings are:")
            buyable = buyableBuilding(eraNumber)
            userBuilding = str(input("\nInput the symbol furthest to the left or cancel to cancel: ")).upper()

        if userBuilding == "CANCEL":
            return [newBoard, newResources, newBuildings]

        purchase = buy(board, resources, eraNumber, userBuilding, plot - 1)
        newBoard = purchase[0]
        newResources = purchase[1]
        input("\nPress enter to continue.")

    else:
        choice = input("\nSelect Upgrade, Demolish, or Info on this Plot or Exit to Leave: ")
        while not (choice == "upgrade" or choice == "demolish" or choice == "info" or choice == "exit"):
            choice = input("\nInvalid Input, Select Upgrade, Demolish, or Info on this Plot or Exit to Leave: ")

        if choice == "exit":
            return [board, resources, buildings]

        elif choice == "upgrade":
            if board[plot - 1][1] == eraNumber:
                print("\n\nThis building is already the maxed level!")
                input("\nPress enter to continue.")

            else:
                confirmation = input("Input yes to confirm purchase or anything else to cancel: ")
                if confirmation == "yes":
                    purchase = buy(board, resources, eraNumber, board[plot - 1][0], plot - 1)
                    newBoard = purchase[0]
                    newResources = purchase[1]
                    input("\nPress enter to continue.")
                else:
                    print("Upgrade cancelled")
                    input("\nPress enter to continue.")

        elif choice == "demolish":
            confirmation = input("Input yes to confirm demolishing or anything else to cancel: ")
            if confirmation == "yes":
                print("\nThe building on plot " + str(plot) + " was successfully demolished.")
                input("\n\nPress enter to continue.")
                buildingType = board[plot - 1][0]
                buildingEra = board[plot - 1][1]
                newBoard[plot - 1] = ["-", 0]
            else:
                print("Demolishing cancelled")
                input("\nPress enter to continue.")

        elif choice == "info":
            replit.clear()
            ages = ["Ancient", "Classical", "Medieval", "Renaissance", "Industrial", "Modern", "Atomic", "Information"]
            names = []
            names.append(["UNDEFINED", "Yurt", "Farm", "UNDEFINED", "UNDEFINED", "UNDEFINED", "UNDEFINED"])
            names.append(["Hospital", "Small House", "Farm", "Blacksmith", "Quarry", "Lumbermill", "UNDEFINED"])
            names.append(["Hospital", "House", "Plantation", "Blacksmith", "Quarry", "Lumbermill", "UNDEFINED"])
            names.append(
                ["Hospital", "Large  House", "Farming Estate", "Gunsmith", "Quarry", "Lumbermill", "UNDEFINED"])
            names.append(["Hospital", "Mansion", "Factory Farms", "Army Camp", "UNDEFINED", "UNDEFINED", "Factory"])
            names.append(["Hospital", "Apartments", "Factory Farms", "Army Camp", "UNDEFINED", "UNDEFINED", "Factory"])
            names.append(["Hospital", "Apartments", "Greenhouse", "Weapons Factory", "UNDEFINED", "UNDEFINED",
                          "Semi-Automated Factory"])
            names.append(["Personal Care", "Capsule Apartments", "GMO Automation Greenhouse and Fishing Farm",
                          "War Machine Factory", "UNDEFINED", "UNDEFINED", "Automated Factory"])
            buildingType = board[plot - 1][0]
            buildingEra = board[plot - 1][1]

            if buildingType == "H":
                print("[" + names[buildingEra][0] + " (Medicine)]\n")
                print("symbol is H, plot number is " + str(plot))
                print("built in the " + ages[buildingEra] + " Era")
                print("provides " + str(hospital[buildingEra]) + "% death prevention")
            elif buildingType == "A":
                print("[" + names[buildingEra][1] + " (Housing)]\n")
                print("symbol is A, plot number is " + str(plot))
                print("built in the " + ages[buildingEra] + " Era")
                print("provides " + str(house[buildingEra]) + " housing population")
            elif buildingType == "P":
                print("[" + names[buildingEra][2] + " (Farming)]\n")
                print("symbol is P, plot number is " + str(plot))
                print("built in the " + ages[buildingEra] + " Era")
                print("supplies " + str(farm[buildingEra]) + " food per turn")
            elif buildingType == "W":
                print("[" + names[buildingEra][3] + " (Military)]\n")
                print("symbol is W, plot number is " + str(plot))
                print("built in the " + ages[buildingEra] + " Era")
                print("provides " + str(weapons[buildingEra]) + " military strength per turn")
            elif buildingType == "L":
                print("[" + names[buildingEra][4] + " (Lumber)]\n")
                print("symbol is L, plot number is " + str(plot))
                print("built in the " + ages[buildingEra] + " Era")
                print("supplies " + str(lumbermill[buildingEra]) + " wood per turn")
            elif buildingType == "S":
                print("[" + names[buildingEra][5] + " (Mining)]\n")
                print("symbol is S, plot number is " + str(plot))
                print("built in the " + ages[buildingEra] + " Era")
                print("supplies " + str(quarryStone[buildingEra]) + " stone and " + str(
                    quarryMetal[buildingEra]) + " metal per turn")
            elif buildingType == "F":
                print("[" + names[buildingEra][6] + " (Production)]\n")
                print("symbol is F, plot number is " + str(plot))
                print("built in the " + ages[buildingEra] + " Era")
                print("supplies " + str(factoryWood[buildingEra]) + " wood, " + str(
                    factoryStone[buildingEra]) + " stone,")
                print(str(factoryMetal[buildingEra]) + " metal, " + str(factorySteel[buildingEra]) + " steel,")
                print(str(factoryCement[buildingEra]) + " cement, " + str(factoryAluminum[buildingEra]) + " aluminum,")
                print(str(factoryTitanium[buildingEra]) + " titanium and , " + str(
                    factoryUranium[buildingEra]) + " uranium per turn")
            input("\n\nPress enter to continue.")

    newBuildings = countBuilding(newBoard)
    return [newBoard, newResources, newBuildings]


# Determines whether or not a event will occur
def eventOccurs(eraNumber):
    value = random.randint(1, 100)
    if value <= eraNumber * eraNumber * eraNumber * eraNumber:
        return True

    return False


# Determines the event that occurs and makes changes accordingly
def eventRun(resources, era):
    newResources = []
    for i in range(len(resources)):
        newResources.append(resources[i])
    value = random.randint(1, 6)
    countryList = ["America", "Great Britian", "France", "Bangladesh", "North Korea", "China", "Venezuela", "Vietnam",
                   "Mozambique", "Madagascar", "Cambodia", "New Zealand", "Peru", "Argentina", "Spain", "Mexico",
                   "Japan", "Taiwan", "Yugoslavia", "Russia", "Ukraine", "Germany", "Sudan", "South Korea", "Morocco",
                   "Sierra Leone", "Chad", "South Africa"]
    country = random.randint(0, len(countryList) - 1)

    # Disease
    if value == 1:
        diseaseList = ["Influenza", "Rabies", "Chicken Pox", "Ebola", "Chlora"]
        num = random.randint(0, len(diseaseList) - 1)
        print("\nA new strand " + diseaseList[num] + " was discovered in " + countryList[
            country] + " and has spread to your country.")
        input("\nPress enter to continue.")
        return [resources, True, False, 0]

    # Trade or Gift
    if value == 2 or value == 3:
        resourceList = ["wood", "stone", "metal", "steel", "cement", "aluminum", "titanium", "uranium", "population",
                        "food", "strength", "gold"]
        if era <= 1:
            num = random.randint(0, 3)
            if num == 2:
                num = 8
            elif num == 3:
                num = 9
        elif era <= 3:
            num = random.randint(0, 6)
            if num == 3:
                num = 8
            elif num == 4:
                num = 9
            elif num == 5:
                num = 10
            elif num == 6:
                num = 11
        elif era <= 5:
            num = random.randint(0, 7)
            if num == 4:
                num = 8
            elif num == 5:
                num = 9
            elif num == 6:
                num = 10
            elif num == 7:
                num = 11
        else:
            num = random.randint(0, len(resourceList) - 1)

        if value == 2 and num == 11:
            num = 9

        if value == 2 and num == 8:
            num = 9

        if value == 2:
            tradeResource = random.randint(1, resources[11] // 4)
            tradeGold = random.randint(1, resources[11] // 2)
            if resources[11] == 0:
                return [resources, False, False, 0]
            if tradeResource == 0 or tradeGold == 0:
                return [newResources, True, False, 0]

            print("\n" + countryList[country] + " would like to trade you " + str(tradeResource) + " " + resourceList[
                num] + " for " + str(tradeGold) + " gold.")

            chose = str(input("\nWould you like to do the trade? yes or no? "))
            while chose != "yes" and chose != "no":
                chose = str(input("\nInvalid input, would you like to do the trade? yes or no? "))

            if chose == "no":
                return [resources, False, False, 0]

            print("\nYou have successfully traded " + str(tradeResource) + " " + resourceList[num] + " for " + str(
                tradeGold) + " gold with " + countryList[country])
            input("\nPress enter to continue.")
            newResources[num] += tradeResource
            newResources[11] -= tradeGold

            return [newResources, False, False, 0]

        else:
            giftAmount = random.randint(1, round(resources[num] // 4))

            if giftAmount == 0:
                giftAmount = 1

            newResources[num] += giftAmount
            if num != 8:
                print("\n" + countryList[country] + " gifted you " + str(giftAmount) + " " + resourceList[num] + "!")
            elif num == 8:
                print("\n" + str(giftAmount) + "immigrants from " + countryList[
                    country] + " and increased your population!")

            return [newResources, False, False, 0]

        input("\nPress enter to continue.")

    # Demand or War
    if value == 4 or value == 5:
        if value == 4:
            if resources[11] == 0:
                return [resources, False, False, 0]

            demandGold = random.randint(1, resources[11])
            print("\n" + countryList[country] + " demands " + str(demandGold) + " gold from you.")
            chose = str(input("\nWould you like to give into the demand? yes or no? "))
            while chose != "yes" and chose != "no":
                chose = str(input("\nInvalid input, would you like to give into the demand? yes or no? "))

            if chose == "yes":
                print("\nYou gave " + countryList[country] + " " + str(demandGold) + " gold.")
                input("\nPress enter to continue.")
                newResources[11] -= demandGold
                return [newResources, False, False, 0]

        if value == 5:
            issueList = ["because of territorial disputes", "for literally no apparent reason",
                         "because they felt like it", "because they believed you were behind an assassination attempt",
                         "because they believed you were behind a bombing",
                         "because they believed you were behind an assassination",
                         "in order to ensure security in the region", "because you made an unfunny joke",
                         "because you politicize wearing masks",
                         "because you care about your political opinion more than the safety of others and yourself",
                         "because you lack common sense", "because they want to exert their influence into you",
                         "because your location could be beneficial as a colony", "because you have natural resources"]
            issue = random.randint(0, len(issueList) - 1)
            print("\n" + countryList[country] + " has decided to go to war on you " + issueList[issue])

        weapons = [0, 2, 5, 25, 250, 500, 10000, 1000000]
        percentDead = round(weapons[era] / (resources[10] + 1) * 100)
        if percentDead > 50:
            percentDead = 50

        print("\n" + str(percentDead) + "% of your population will be killed.")
        input("\nPress enter to continue.")
        return [resources, False, True, percentDead]

    return [resources, False, False, 0]


# Runs the final stage of the game
def finalStageRun(resources, turnsLeft, finalStageType):
    # Build and Escape (1), Fight (2), Build (3)
    alien = ["an Alien Invasion", 2]
    war = ["a Nuclear War", 1]
    disease = ["a Disease", 3]
    meteor = ["a Meteor", 1]
    volcano = ["a Volcanic Eruption", 1]

    issueList = []
    issueList.append(alien)
    issueList.append(war)
    issueList.append(disease)
    issueList.append(meteor)
    issueList.append(volcano)
    if turnsLeft == 5:
        if finalStageType == 0:
            print("Government agencies from around the world have detected " + issueList[
                finalStageType] + " in approximately 5 years with the capabilities to make humans become extinct.")
        elif finalStageType == 1:
            print(
                "Rising tensions between world superpowers and the recent increase in the development of nuclear weapons in second and third world countries is believed to cause " +
                issueList[finalStageType] + " in 5 years and could turn the world into a wasteland.")
        else:
            print("Top scientists from around the world have determined that in approximately 5 years, there will be " +
                  issueList[finalStageType] + " with the capabilities to wipe out the entire world.")

    elif turnsLeft != 0:
        print(
            "In " + turnsLeft + "years, " + issueList[finalStageType][0] + " will occur and threaten your population.")

    # resources = [wood, stone, metal, steel, cement, aluminum, titanium, uranium, population, food, strength, gold]
    # Build and Escape
    if issueList[finalStageType][1] == 1:
        reqSteel = 500000000
        reqAluminum = 500000
        reqTitanium = 50000
        reqUranium = 1000

        if resources[3] >= reqSteel and resources[5] >= reqAluminum and resources[6] >= reqTitanium and resources[
            7] >= reqUranium:
            return [False, True]

        if turnsLeft != 0:
            if resources[3] < reqSteel:
                print("You need " + str(reqSteel) + " steel, but you only have " + str(resources[3]))
            if resources[5] < reqAluminum:
                print("You need " + str(reqAluminum) + " aluminum, but you only have " + str(resources[5]))
            if resources[6] < reqTitanium:
                print("You need " + str(reqTitanium) + " titanium, but you only have " + str(resources[6]))
            if resources[7] < reqUranium:
                print("You need " + str(reqUranium) + " uranium, but you only have " + str(resources[7]))

    # Fight
    elif issueList[finalStageType][1] == 2:
        reqStrength = 50000000

        if resources[10] >= reqStrength:
            return [False, True]

        if turnsLeft != 0:
            print("You need " + str(reqStrength) + " military strength, but you only have " + str(resources[10]))

    # Build
    elif issueList[finalStageType][1] == 3:
        reqSteel = 100000000
        reqCement = 10000000
        reqAluminum = 100000
        reqTitanium = 10000
        reqUranium = 1000

        if resources[3] >= reqSteel and resources[4] >= reqCement and resources[5] >= reqAluminum and resources[
            6] >= reqTitanium and resources[7] >= reqUranium:
            return [False, True]

        if turnsLeft != 0:
            if resources[3] < reqSteel:
                print("You need " + str(reqSteel) + " steel, but you only have " + str(resources[3]))
            if resources[4] < reqCement:
                print("You need " + str(reqCement) + " cement, but you only have " + str(resources[4]))
            if resources[5] < reqAluminum:
                print("You need " + str(reqAluminum) + " aluminum, but you only have " + str(resources[5]))
            if resources[6] < reqTitanium:
                print("You need " + str(reqTitanium) + " titanium, but you only have " + str(resources[6]))
            if resources[7] < reqUranium:
                print("You need " + str(reqUranium) + " uranium, but you only have " + str(resources[7]))

    if turnsLeft == 0:
        return [True, False]

    return [False, False]


# // MAIN // #

answer = ""
while answer != "exit":
    replit.clear()
    start()
    answer = input("")

    # Exits the program if the player wants to exit
    if answer == "exit":
        replit.clear()
        break

    # Runs the tutorial if the player wants the tutorial
    elif answer == "tutorial":
        replit.clear()
        tutorial()

    # Starts the game if the player wants to play
    elif answer == "play":
        replit.clear()
        # Board Setup
        board = setupBoard()

        # Time Setup
        turn = 0
        year = 4000
        calender = "BCE"
        era = "Ancient Era"
        eraNumber = 0
        time = [turn, year, calender, era, eraNumber]

        # Resource Setup
        wood = 100
        stone = 25
        metal = 0
        steel = 0
        cement = 0
        aluminum = 0
        titanium = 0
        uranium = 0
        gold = 0

        population = 2
        food = 10
        strength = 0

        resources = [wood, stone, metal, steel, cement, aluminum, titanium, uranium, population, food, strength, gold]

        # Building Setup
        buildings = countBuilding(board)

        # Keeps running until the player losses (pop = 0)
        lost = False
        won = False
        finalStageType = random.randint(0, 4)
        turnsLeft = 5
        while not lost and not won:
            replit.clear()
            maxpop = maxPop(buildings[1])
            eraNumber = time[4]
            event = eventOccurs(eraNumber)
            disease = False
            war = False
            percentDead = 0

            if time[1] >= 2200 and time[4] == 7:
                winloss = finalStageRun(resources, turnsLeft, finalStageType)
                lost = winloss[0]
                won = winloss[1]
                turnsLeft -= 1

            if event == True and won == False and lost == False:
                fullPrint(time, resources, board, maxpop, buildings, eraNumber, disease, war, percentDead)
                eventOutput = eventRun(resources, time[4])
                resources = eventOutput[0]
                disease = eventOutput[1]
                war = eventOutput[2]
                percentDead = eventOutput[3]

            fullPrint(time, resources, board, maxpop, buildings, eraNumber, disease, war, percentDead)

            endTurn = False

            if won != False or lost != False:
                endTurn = True

            while not endTurn:
                fullPrint(time, resources, board, maxpop, buildings, eraNumber, disease, war, percentDead)
                newInformation = changeGame(board, resources, buildings, eraNumber, maxpop, disease, war, percentDead)

                if newInformation[0] == "end":
                    endTurn = True

                else:
                    board = newInformation[0]
                    resources = newInformation[1]
                    buildings = countBuilding(board)
                    maxpop = maxPop(buildings[1])

            buildings = countBuilding(board)
            time = timeChange(time)
            resources = resourcesChange(resources, buildings, eraNumber, maxpop, disease, war, percentDead)
            lost = lostGame(resources[8])

        if won:
            replit.clear()
            print("You won the game!")
            input("\nPress enter to continue.")
        elif lost:
            replit.clear()
            print("You lost the game, better luck next time")
            input("\nPress enter to continue.")