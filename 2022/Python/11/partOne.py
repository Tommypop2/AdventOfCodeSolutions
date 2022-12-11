from math import floor
monkeys: list[list[str]] = []
test = []


def getIndexes(pattern: str, arr: list):
    indexes = []
    for i, item in enumerate(arr):
        if (pattern == item):
            indexes.append(i)
    return indexes


contents = open("in.txt").read().splitlines()
indexes = [0] + getIndexes("", contents) + [len(contents)]
for i in range(1, len(indexes)):
    monkey = contents[indexes[i - 1]: indexes[i]]
    monkey = list(filter(lambda x: x != "", monkey))
    x = []
    x.append(monkey[0].replace("Monkey ", "")[0:-1])
    x.append(list(map(int,monkey[1].strip().replace("Starting items: ", "").split(","))))
    x.append(monkey[2].replace("Operation: new = old ", "").strip().split(" "))
    test = []
    test.append(int(monkey[3].strip().replace("Test: divisible by ", "")))
    test.append(int(monkey[4].strip().replace(
        "If true: throw to monkey ", "")))
    test.append(int(monkey[5].strip().replace(
        "If false: throw to monkey ", "")))
    x.append(test)
    monkeys.append(x)


def doOperation(old: int, operation: str):
    old = int(old)
    operator = operation[0]
    value = operation[1]
    if (value == "old"):
        value = old
    value = int(value)
    if (operator == "+"):
        return old + value
    elif (operator == "-"):
        return old - value
    elif (operator == "*"):
        return old * value
    return old / value
monkeyInspections = [0 for _ in range(len(monkeys))]
round = 0
while True:
    round += 1
    for i in range(len(monkeys)):
        items = monkeys[i][1]
        operation = monkeys[i][2]
        test = monkeys[i][3]
        itemsToRemove = []
        for n in items:
            monkeyInspections[i] += 1
            worryLevel = doOperation(n, operation)
            worryLevel = floor(worryLevel / 3)
            if(worryLevel % int(test[0]) == 0):
                monkeys[test[1]][1].append(worryLevel)
            else:
                monkeys[test[2]][1].append(worryLevel)
            itemsToRemove.append(n)
        for k in itemsToRemove:
            monkeys[i][1].remove(k)
            itemsToRemove = []
    if (round == 20):
        break
monkeyInspections.sort(reverse=True)
print(monkeyInspections[0] * monkeyInspections[1])