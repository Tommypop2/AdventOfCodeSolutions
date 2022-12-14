fC = open("input.txt").read().splitlines()
t = 0
for i in fC:
    a, b = i.split(" ")
    a = ord(a) - ord("A")
    b = ord(b) - ord("X")
    if (b == 0):
        t += (a-1) % 3 + 1
    if (b == 1):
        t += 3 + a + 1
    if (b == 2):
        t += 6 + (a+1) % 3 + 1
print(t)
