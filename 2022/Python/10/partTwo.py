cycle = 0
xval = 1
o = []
total = 0
display = [["." for _ in range(40)] for _ in range(6)]
def yes():
    o.append((cycle, xval))

def render():
    for i in display:
        for n in i:
            print(n, end="")
        print()
for i in open("in.txt").read().splitlines():
    if(i == "noop"):
        cycle += 1
        yes()
    elif(i.startswith("addx ")):
        n = i.replace("addx ", "")
        cycle += 1
        yes()
        cycle += 1
        yes()
        xval += int(n)
count = 0
for i in range(6):
    for n in range(40):
        count += 1
        display[i][n] = "#" if o[count - 1][1] >= n-1 and o[count-1][1] <= n + 1 else "."

render()