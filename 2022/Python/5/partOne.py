with open("input.txt", "r") as f:
    file = f.readlines()

diagram = file[:file.index("\n")]
diagram = list(map(lambda x: x.replace("\n", ""), diagram))
instructions = file[file.index("\n") + 1:]

numbers = diagram[-1]
i = 0
numArr = []
while True:
    i += 1
    try:
        index = numbers.index(str(i))
    except ValueError:
        break
    numArr.append(index)

stacks = []

for i in numArr:
    stack = []
    index = len(diagram) - 2
    while True:
        if (index < 0):
            break
        value = diagram[index][i]
        if (value == " "):
            break
        stack.append(value)
        index -= 1
    stacks.append(stack)
# print(stacks)
for i in instructions:
    numToMove = int(i.split("move")[1].split("from")[0].strip())
    whereFrom = int(i.split("from")[1].split("to")[0].strip())
    whereTo = int(i.split("to")[1].strip())
    stack = stacks[whereFrom - 1]
    newStack = stack[:-numToMove]
    stuffToAppend = stack[-numToMove:]
    stacks[whereTo - 1] = stacks[whereTo - 1] + list(reversed(stuffToAppend))
    stacks[whereFrom - 1] = newStack
output = ""
for i in stacks:
    output += i[-1]
print(output)
