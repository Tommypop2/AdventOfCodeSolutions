with open("input.txt", "r") as f:
    dataStream = f.readlines()[0]
for i in range(14, len(dataStream)):
    lastChars = dataStream[i-14:i]
    chars = []
    for n in lastChars:
        if(n in chars):
            break
        chars.append(n)
    else:
        print(i)
        break