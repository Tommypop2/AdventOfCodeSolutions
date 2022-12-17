import re
yRange = 4000000
pattern = re.compile('\-*\d+')
fC = open("in.txt").read().splitlines()
contents = [list(map(int, pattern.findall(line))) for line in fC]
for YVAL in range(yRange + 1):
    intervals = []
    for sX, sY, bX, bY in contents:
        dX = abs(sX - bX)
        dY = abs(sY - bY)
        d = dX + dY
        offset = d - abs(sY - YVAL)
        if (offset < 0):
            continue
        intervals.append((sX - offset, sX + offset))

    intervals.sort()
    q = []

    for low, high in intervals:
        if not q:
            q.append([low, high])
            continue
        qlow, qhigh = q[-1]
        if (low > qhigh + 1):
            q.append([low, high])
            continue
        q[-1][1] = max(qhigh, high)

    x = 0
    for low, high in q:
        if (x < low):
            print(x * 4000000 + YVAL)
            exit(0)
        x = max(x, high + 1)
        if (x > yRange):
            break
