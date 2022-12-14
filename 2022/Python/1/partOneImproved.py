fC = open("input.txt").read().splitlines()
total = 0
currentMax = 0
for i in fC:
    if(i == ""):
        currentMax = total if total > currentMax else currentMax
        total = 0
        continue
    total += int(i)
print(currentMax)