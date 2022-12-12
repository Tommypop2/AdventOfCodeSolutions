from math import sqrt
visitedSquares = set()
def getDistance(currentPos: complex, endPos: complex):
    distance = sqrt(abs(currentPos.real - endPos.real) ** 2 +
                    abs(currentPos.imag - endPos.imag) ** 2)
    return distance

def getNextPos(currentPos: complex, endPos: complex, heightMap: list[list[str]]):
    heightMapHeight = len(heightMap)
    heightMapWidth = len(heightMap[0])
    moves = [currentPos + 1j, currentPos -
                     1j, currentPos + 1, currentPos - 1]
    # if(moves[2] == 3):
    #     breakpoint()
    possibleMoves: list[complex] = []
    for item in moves:
        if(item.imag < 0 or item.imag >= heightMapHeight or item.real < 0 or item.real >= heightMapWidth):
            continue
        charAtCurrent = heightMap[int(currentPos.imag)][int(currentPos.real)]
        charAtNext = heightMap[int(item.imag)][int(item.real)]
        currentPosCode = ord(charAtCurrent)
        nextPosCode = ord(charAtNext)
        if(nextPosCode - currentPosCode > 1):
            continue
        if(item in visitedSquares):
            continue
        possibleMoves.append(item)
    bestMove = possibleMoves[0]
    for i in range(1, len(possibleMoves)):
        if(getDistance(possibleMoves[i], endPos) < getDistance(bestMove, endPos)):
            bestMove = possibleMoves[i]
    return bestMove


fileContents = [list(x) for x in open("in.txt").read().splitlines()]
startingPos = 0
endPos = 0
for i in enumerate(fileContents):
    for n in enumerate(i[1]):
        if (n[1] == "S"):
            startingPos = (i[0]) * 1j + n[0]
        elif (n[1] == "E"):
            endPos = (i[0]) * 1j + n[0]

heightMap = list(
    map(lambda x: list(map(lambda y: y.lower(), x)), fileContents))
heightMap[int(endPos.imag)][int(endPos.real)] = "z"
heightMap[int(startingPos.imag)][int(startingPos.real)] = "a"
currentPos = startingPos
numOfMoves = 0
while True:
    numOfMoves += 1
    currentPos = getNextPos(currentPos, endPos, heightMap)
    visitedSquares.add(currentPos)
    if(currentPos == endPos):
        break
print(startingPos, endPos)
print(numOfMoves)