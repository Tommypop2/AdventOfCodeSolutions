import re
minX = 0
maxX = 0
YVAL = 2000000
pattern = re.compile('\-*\d+')
impossible = set()
beacons = set()
for i in open("in.txt").read().splitlines():
    sX, sY, bX, bY = map(int, pattern.findall(i))
    beacons.add((bX, bY))
    minX = min(sX, bX, minX)
    maxX = max(sX, bX, maxX)
    dX = abs(sX - bX)
    dY = abs(sY - bY)
    d = dX + dY
    offset = d - abs(sY - YVAL)
    if (offset < 0):
        continue
    for n in range(sX - offset, sX + offset + 1):
        impossible.add((n, YVAL))

print(len(impossible - beacons))
