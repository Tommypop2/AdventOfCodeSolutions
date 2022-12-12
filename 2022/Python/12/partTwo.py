from collections import deque # Double ended queue
# Breadth first search
heightMap = [list(x) for x in open("in.txt").read().strip().splitlines()]
startingPos = 0
endPos = 0
for i in enumerate(heightMap):
    for n in enumerate(i[1]):
        if (n[1] == "S"):
            startingPos = (i[0]) * 1j + n[0]
        elif (n[1] == "E"):
            endPos = (i[0]) * 1j + n[0]

heightMap[int(endPos.imag)][int(endPos.real)] = "z"
heightMap[int(startingPos.imag)][int(startingPos.real)] = "a"

visited = {endPos}

queue = deque()
queue.append((0, endPos)) # Initial State (distance, location)

while queue:
    dis, pos = queue.popleft()
    for newPos in [pos + 1j, pos - 1j, pos + 1, pos - 1]:
        if(newPos.imag < 0 or newPos.real < 0 or newPos.real >= len(heightMap[0]) or newPos.imag >= len(heightMap)):
            continue
        if(newPos in visited):
            continue
        if(ord(heightMap[int(newPos.imag)][int(newPos.real)]) - ord(heightMap[int(pos.imag)][int(pos.real)]) < -1):
            continue
        if (heightMap[int(newPos.imag)][int(newPos.real)] == "a"):
            print(dis + 1)
            exit(0)
        visited.add(newPos)
        queue.append((dis + 1, newPos))