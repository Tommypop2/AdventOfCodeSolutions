import ast
def compareVal(item1, item2):
    if(type(item1) == int and type(item2) == int):
        if(item1 < item2):
            return 0 # true
        elif(item1 > item2):
            return -1 # false
        else:
            return 1 # next
    elif(type(item1) == list and type(item2) == list):
        for i in range(max(len(item1), len(item2))):
            if(i >= len(item1) and i < len(item2)):
                return 0
            elif(i >= len(item2) and i < len(item1)):
                return -1
            result = compareVal(item1[i], item2[i])
            if(result == 0):
                return 0
            elif(result == -1):
                return -1
        return 1
    else:
        if(type(item1) == int):
            item1 = [item1]
        if(type(item2) == int):
            item2 = [item2]
        return compareVal(item1, item2)
def getBool(yes):
    return True if yes == 0 else False
contents = list(filter(lambda x: x.strip() != "", open("in.txt").read().splitlines()))
pairs = 0
correctPairs = []
for i in range(0, len(contents), 2):
    pairs += 1
    item1 = ast.literal_eval(contents[i])
    item2 = ast.literal_eval(contents[i + 1])
    if getBool(compareVal(item1,item2)) == True:
        correctPairs.append(pairs)
print(sum(correctPairs))