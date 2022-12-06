with open("input.txt", "r") as f:
    pairs = f.readlines()
numOfPairs = 0
for pair in pairs:
    pair = pair.strip()
    elf1, elf2 = pair.split(",")
    elf1Min, elf1Max = list(map(lambda x: int(x), elf1.split("-")))
    elf2Min, elf2Max = list(map(lambda x: int(x), elf2.split("-")))
    if ((elf1Min >= elf2Min and elf1Max <= elf2Max and elf1Max >= elf2Min) or (elf2Min >= elf1Min and elf2Max <= elf1Max and elf2Max >= elf1Min)):
        numOfPairs += 1
print(numOfPairs)