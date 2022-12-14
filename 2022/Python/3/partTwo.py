def getDuplicates(one, two, three):
    for i in one:
        for n in two:
            if (i == n and i in three):
                return i


def getPriorities(duplicates):
    prioritySum = 0
    for i in duplicates:
        characterCode = ord(i)
        if (characterCode > 90):  # If letter is lower case
            priority = characterCode - 96
        else:
            priority = characterCode - 38
        prioritySum += priority
    return prioritySum


with open("input.txt", "r") as f:
    rucksacks = f.readlines()
prioritySum = 0
for i in range(0, len(rucksacks), 3):
    rucksackOne = rucksacks[i].strip()
    rucksackTwo = rucksacks[i + 1].strip()
    rucksackThree = rucksacks[i + 2].strip()
    prioritySum += getPriorities(getDuplicates(rucksackOne,
                                 rucksackTwo, rucksackThree))
print(prioritySum)
