fC = open("input.txt").read().splitlines()
total = 0
for i in range(0, len(fC), 3):
    n = list(set(fC[i]) & set(fC[i + 1]) & set(fC[i+2]))[0]
    total += ord(n) - (38 if ord(n) < 96 else 96)
print(total)