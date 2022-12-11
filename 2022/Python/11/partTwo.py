monkeys = []


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
    x.append(list(map(int, monkey[1].strip().replace(
        "Starting items: ", "").split(","))))
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

# (a + b) mod x = ((a mod x) + (b mod x)) mod x
# apparently
# (a * b) mod x = ((a mod x) * (b mod x)) mod x

mod = 1
for monkey in monkeys:
    mod *= monkey[3][0]
monkeyInspections = [0 for _ in range(len(monkeys))]
for _ in range(10000):
    for i in range(len(monkeys)):
        items = monkeys[i][1][:]
        operation = monkeys[i][2]
        test = monkeys[i][3]
        for n in items:
            monkeyInspections[i] += 1
            worryLevel = doOperation(n, operation)
            worryLevel %= mod
            # worryLevel = floor(worryLevel / 3)
            if (worryLevel % test[0] == 0):
                monkeys[test[1]][1].append(worryLevel)
            else:
                monkeys[test[2]][1].append(worryLevel)
            monkeys[i][1].remove(n)
monkeyInspections.sort(reverse=True)
print(monkeyInspections[0] * monkeyInspections[1])
