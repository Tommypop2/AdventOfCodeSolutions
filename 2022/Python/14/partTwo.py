fC = open("in.txt").read().splitlines()


def getNewpositions(item: complex, nItem: complex):
    if (item.real == nItem.real):
        iDiff = item.imag - nItem.imag
        if (iDiff > 0):
            return set(map(lambda x: x * 1j + item.real, set(range(int(nItem.imag), int(item.imag) + 1))))
        else:
            return set(map(lambda x: x * 1j + item.real, set(range(int(item.imag), int(nItem.imag) + 1))))
    if (item.imag == nItem.imag):
        rDiff = item.real - nItem.real
        if (rDiff > 0):
            return set(map(lambda x: x + item.imag * 1j, set(range(int(nItem.real), int(item.real) + 1))))
        else:
            return set(map(lambda x: x + item.imag * 1j, set(range(int(item.real), int(nItem.real) + 1))))


sP = 500 + 0j

rPs: set[complex] = set()
maxYval = 0
for i in fC:
    elems = list(
        map(lambda x: int(x.split(",")[0]) + int(x.split(",")[1]) * 1j, i.split("->")))
    for n in range(len(elems) - 1):
        item = elems[n]
        nItem = elems[n + 1]
        newPositions = getNewpositions(item, nItem)
        rPs = rPs.union(newPositions)
for i in rPs:
    if (i.imag > maxYval):
        maxYval = i.imag
floorVal = maxYval + 2
currentSandPos = sP
restingSand = 0
while True:
    if ((currentSandPos + 1j).imag == floorVal):
        restingSand += 1
        rPs.add(currentSandPos)
        currentSandPos = sP
        continue
    if (currentSandPos + 1j not in rPs):
        currentSandPos += 1j
    elif (currentSandPos + 1j - 1 not in rPs):
        currentSandPos += 1j - 1
    elif (currentSandPos + 1j + 1 not in rPs):
        currentSandPos += 1j + 1
    else:
        restingSand += 1
        rPs.add(currentSandPos)
        if (currentSandPos == sP):
            break
        currentSandPos = sP

print(restingSand)
