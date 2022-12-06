with open("input.txt", "r") as f:
    pairs = f.readlines()
numOfPairs = 0
for pair in pairs:
    pair = pair.strip()
    elf1, elf2 = pair.split(",")
    elf1Min, elf1Max = list(map(lambda x: int(x), elf1.split("-")))
    elf2Min, elf2Max = list(map(lambda x: int(x), elf2.split("-")))
    elf1Range = list(range(elf1Min, elf1Max + 1))
    elf2Range = list(range(elf2Min, elf2Max + 1))
    for i in elf1Range:
        if(i in elf2Range):
            numOfPairs += 1
            break
print(numOfPairs)