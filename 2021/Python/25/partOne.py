from time import sleep


def printBoard(columns):
    print("-------------------")
    for row in columns:
        for item in row:
            print(item, end="")
        print(end="\n")
    print("------------------")


file = open("input.txt").read().splitlines()

columns = [list(i) for i in file]

steps = 0
eastUrchinsToMove = []
southUrchinsToMove = []
while True:
    changes = 0
    # printBoard(columns)
    eastUrchinsToMove = []
    southUrchinsToMove = []
    for i in range(len(columns)):
        row = columns[i]
        skip = False
        for n in range(len(row)):
            if (skip == True):
                skip = False
                continue
            current = columns[i][n]
            if (n + 2 > len(row)):
                n = -1
            next = columns[i][n + 1]
            if (current == ">" and next == "."):
                eastUrchinsToMove.append((i, n))
                skip = True
                changes += 1
    for i in eastUrchinsToMove:
        columns[i[0]][i[1]] = "."
        columns[i[0]][i[1] + 1] = ">"
    for i in range(len(columns[0])):
        skip = False
        for n in range(len(columns)):
            if (skip == True):
                skip = False
                continue
            current = columns[n][i]
            if (n + 2 > len(columns)):
                n = -1
            next = columns[n + 1][i]
            if (current == "v" and next == "."):
                southUrchinsToMove.append((n, i, "south"))
                skip = True
                changes += 1
    for i in southUrchinsToMove:
        columns[i[0]][i[1]] = "."
        columns[i[0] + 1][i[1]] = "v"
    steps += 1
    if (changes == 0):
        break
print(steps)
