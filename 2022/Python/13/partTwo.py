import ast


def compareVal(item1, item2):
    if (type(item1) == int and type(item2) == int):
        if (item1 < item2):
            return 0  # true
        elif (item1 > item2):
            return -1  # false
        else:
            return 1  # next
    elif (type(item1) == list and type(item2) == list):
        for i in range(max(len(item1), len(item2))):
            if (i >= len(item1) and i < len(item2)):
                return 0
            elif (i >= len(item2) and i < len(item1)):
                return -1
            result = compareVal(item1[i], item2[i])
            if (result == 0):
                return 0
            elif (result == -1):
                return -1
        return 1
    else:
        if (type(item1) == int):
            item1 = [item1]
        if (type(item2) == int):
            item2 = [item2]
        return compareVal(item1, item2)


contents = list(filter(lambda x: x.strip() != "",
                open("in.txt").read().splitlines()))
contents = list(map(lambda x: ast.literal_eval(str(x)), contents))
contents.append([[2]])
contents.append([[6]])
while True:
    swaps = 0
    for i in range(0, len(contents) - 1):
        item1 = contents[i]
        item2 = contents[i + 1]
        if (compareVal(item1, item2) == -1):
            contents[i] = item2
            contents[i + 1] = item1
            swaps += 1
    if (swaps == 0):
        break

print((contents.index([[2]]) + 1) * (contents.index([[6]]) + 1))
