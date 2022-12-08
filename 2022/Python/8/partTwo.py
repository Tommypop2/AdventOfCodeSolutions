file = open("in.txt").read().splitlines()
trees = [list(i) for i in file]
width = len(trees[0])
height = len(trees)
outside = (width * height) - (width - 2) * (height - 2)
total = outside


def calcVisibleTrees(treeHeight, arr):
    scenicScore = 0
    for i in arr:
        if (treeHeight > i):
            scenicScore += 1
        if(treeHeight <= i):
            scenicScore += 1
            break
    return scenicScore


maxScenicScore = 0
for i in range(1, len(trees) - 1):
    for n in range(1, len(trees[0]) - 1):
        tree = int(trees[i][n])
        right = list(map(int, trees[i][n + 1:len(trees[0]) + 1]))
        left = list(map(int, trees[i][0:n]))
        bottom = [int(x[n]) for x in trees[i + 1: len(trees) + 1]]
        top = [int(x[n]) for x in trees[0:i]]
        topScore = calcVisibleTrees(tree, top[::-1])
        bottomScore = calcVisibleTrees(tree, bottom)
        leftScore = calcVisibleTrees(tree, left[::-1])
        rightScore = calcVisibleTrees(tree, right)
        scenicScore = topScore * bottomScore * leftScore * rightScore
        if(scenicScore > maxScenicScore):
            maxScenicScore = scenicScore

print(maxScenicScore)