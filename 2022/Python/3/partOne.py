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


def getDuplicates(str1, str2):
    duplicates = []
    for i in str1:
        if (i in str2):
            duplicates.append(i)
    return duplicates


with open("input.txt", "r") as f:
    rucksacks = f.readlines()
duplicates = []
for rucksack in rucksacks:
    rucksack = rucksack.strip()
    halfLength = int(len(rucksack) / 2)
    compartmentOne = rucksack[:halfLength]
    compartmentTwo = rucksack[halfLength:]
    duplicateValues = getDuplicates(compartmentOne, compartmentTwo)
    duplicates.append(duplicateValues[0])
print(getPriorities(duplicates))
