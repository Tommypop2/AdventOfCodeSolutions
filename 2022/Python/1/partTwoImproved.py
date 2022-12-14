fC = open("input.txt").read().splitlines()
t = 0
arr = []
for i in fC:
    if(i == ""):
        arr.append(t)
        t = 0
        continue
    t += int(i)
arr.sort(reverse=True)
print(sum(arr[:3]))