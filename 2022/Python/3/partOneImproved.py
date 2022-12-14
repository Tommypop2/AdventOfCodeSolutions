ruckSacks = open("testInput.txt").read().splitlines()
total = 0
for i in ruckSacks:
    mid = len(i) // 2
    intersection = set(i[:mid]) & set(i[mid:])
    for n in intersection:
        total += ord(n) - (38 if ord(n) < 96 else 96)
print(total)