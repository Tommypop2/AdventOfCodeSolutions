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
for i in range(len(elftotals) - 1):
    index = i + 1
    while index > 0:
        if(elftotals[index - 1] < elftotals[index]):
            temp = elftotals[index - 1] 
            elftotals[index - 1] = elftotals[index]
            elftotals[index] = temp
        index -= 1
total = 0
for i in range(3):
    total += elftotals[i]

print(total)