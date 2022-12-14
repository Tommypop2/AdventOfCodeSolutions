fC = open("input.txt").read().splitlines()
t = 0
for i in fC:
    a, b = i.split(",")
    aS = a.split("-")
    aR = set(range(int(aS[0]), int(aS[1]) + 1))
    bS = b.split("-")
    bR = set(range(int(bS[0]), int(bS[1]) + 1))
    if len(aR & bR) == len(aR) or len(aR & bR) == len(bR):
        t += 1

print(t)
