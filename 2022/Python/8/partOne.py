file = open("test.txt").read().splitlines()
trees = [list(i) for i in file]
width = len(trees[0])
height = len(trees)
outside = (width * height) - (width - 2) * (height - 2)
total = outside
for i in range(1, len(trees) - 1):
    for n in range(1, len(trees[0]) - 1):
        tree = int(trees[i][n])
        right = list(map(int, trees[i][n + 1:len(trees[0]) + 1]))
        left = list(map(int, trees[i][0:n]))
        bottom = [int(x[n]) for x in trees[i + 1: len(trees) + 1]]
        top = [int(x[n]) for x in trees[0:i]]
        if (tree > max(right) or tree > max(left) or tree > max(bottom) or tree > max(top)):
            total += 1

print(total)
