fC = open("input.txt").read().splitlines()
t = 0
for i in fC:
    a, b = i.split(" ")
    a = ord(a) - ord("A")
    b = ord(b) - ord("X")
    if(a == b):
        t += 3
    elif(b - a) % 3 == 1:
        t += 6
    t += b + 1
print(t)