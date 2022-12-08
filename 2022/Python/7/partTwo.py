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
totalSpace = 70000000
requiredFree = 30000000

spaceUsed = sizes[0]

spaceFree = totalSpace - spaceUsed

extraRequired = requiredFree - spaceFree
min = sizes[0]
minIndex = 0
for i, item in enumerate(sizes):
    if (item >= extraRequired and item < min):
        min = item
print(min)
