fileContents = list(
    map(lambda x: x.split(), open("in.txt").read().splitlines()))
positions = [0 for _ in range(10)]
oldHeadPosition = 0
tailPositions = []


def genTailOffset(headPosition: complex, tailPosition: complex): #This function is inspired by hyper neutrino's solution.
    #It works the same as my function in partOne, but it just takes fewer lines
    offset = 0
    dx = headPosition.real - tailPosition.real
    dy = headPosition.imag - tailPosition.imag
    if(abs(dx) > 1 or abs(dy) > 1):
        if(dx == 0):
            offset += (dy // 2) * 1j
        elif(dy == 0):
            offset += dx // 2
        else:
            offset += 1 if dx > 0 else -1
            offset += 1j if dy > 0 else -1j
    return offset


for n in fileContents:
    direction = n[0]
    steps = int(n[1])
    for _ in range(steps):
        posOffset = 1 if direction == "R" else - \
            1 if direction == "L" else 1j if direction == "U" else -1j
        positions[0] += posOffset
        for i in range(9):
            positions[i+1] += genTailOffset(positions[i], positions[i+1])
        tailPositions.append(positions[-1])
print(len(set(tailPositions)))
