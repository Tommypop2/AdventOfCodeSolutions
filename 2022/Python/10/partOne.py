cycles = 0
xval = 1
indexes = [20,60,100,140,180,220]
total = 0
def yes():
    global total
    if(cycles in indexes):
        total += cycles * xval
        print(cycles, xval)
for i in open("in.txt").read().splitlines():
    if(i == "noop"):
        cycles += 1
        yes()
    elif(i.startswith("addx ")):
        n = i.replace("addx ", "")
        cycles += 1
        yes()
        cycles += 1
        yes()
        xval += int(n)

print(total)