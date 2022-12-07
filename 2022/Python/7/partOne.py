with open("input.txt", "r") as f:
    contents = f.readlines()


def getSize(tree, directory):
    dir: list[str] = tree[directory]
    total = 0
    for i in dir:
        if (i[0].isdigit()):
            total += int(i.split(" ")[0])
    return total


tree = {}
currentDir = ""
dirs = []
for index, i in enumerate(contents):
    if ("$ cd " in i):
        newDir = i.replace("$ cd ", "").strip()
        if (newDir == ".."):
            reverse = currentDir[::-1]
            index = reverse.index("/", 1)
            currentDir = reverse[index:][::-1]
        else:
            if (newDir != "/"):
                currentDir += newDir + "/"
            else:
                currentDir = "/"
        if (currentDir not in tree):
            tree[currentDir] = []
        continue
    if ("$ ls" in i):
        continue
    tree[currentDir].append(i.strip())
total = 0
sizes = []
for i in tree:
    i = str(i)
    size = 0
    for n in tree.keys():
        n = str(n)
        if (n.startswith(i)):
            size += (getSize(tree, n))
    # print(i, size)
    sizes.append(size)

total = 0
for i in sizes:
    if (i <= 100000):
        total += i
print(total)
