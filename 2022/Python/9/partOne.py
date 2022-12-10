fileContents = list(
    map(lambda x: x.split(), open("in.txt").read().splitlines()))
headPosition = 0
tailPosition = 0
tailPositions = []


def genTailOffset(headPosition: complex, tailPosition: complex):
    offset = 0
    if (headPosition.real != tailPosition.real and headPosition.imag != tailPosition.imag):
        if (abs(headPosition.real - tailPosition.real) > 1):
            offset = (1 if (headPosition.real - tailPosition.real) > 0 else -1) + \
                (1j if (headPosition.imag - tailPosition.imag) > 0 else -1j)
        if (abs(headPosition.imag - tailPosition.imag) > 1):
            offset = (1 if (headPosition.real - tailPosition.real) > 0 else -1) + \
                (1j if (headPosition.imag - tailPosition.imag) > 0 else -1j)
        return offset
    if (abs(headPosition.real - tailPosition.real) > 1):
        offset += 1 if headPosition.real > tailPosition.real else -1
    if (abs(headPosition.imag - tailPosition.imag) > 1):
        offset += 1j if headPosition.imag > tailPosition.imag else -1j
    return offset


for n in fileContents:
    direction = n[0]
    steps = int(n[1])
    for i in range(steps):
        posOffset = 1 if direction == "R" else - \
            1 if direction == "L" else 1j if direction == "U" else -1j
        headPosition += posOffset
        tailPositions.append(tailPosition)
        tailPosition += genTailOffset(headPosition, tailPosition)
    tailPositions.append(tailPosition)
print(len(set(tailPositions)))
