with open("input.txt", "r") as f:
    lines = f.readlines()
elftotals = []
currentTotal = 0
for i in lines:
    if(i.strip() == ""):
        elftotals.append(currentTotal)
        currentTotal = 0
        continue
    currentTotal += int(i)
currentMax = elftotals[0]
index = 0
for i in range(1, len(elftotals)):
    if(elftotals[i] > currentMax):
        currentMax = elftotals[i]
        index = i
print(currentMax, index)