from math import floor
variables = {"w": 0, "x": 0, "y": 0, "z": 0}

contents = open("instripped.txt").read().splitlines()

inputBuffer = "99394899891971" * 14
inputIndex = 0


def generateNewInput():
    global inputBuffer
    tempBuffer = inputBuffer
    while True:
        tempBuffer = str(int(tempBuffer) + 1)
        if ("0" not in tempBuffer):
            inputBuffer = tempBuffer
            break


def parseInstruction(instruction: str):
    global inputIndex
    if (instruction.startswith("inp ")):
        variableName = instruction.replace("inp ", "").strip()
        variableValue = int(inputBuffer[inputIndex])
        variables[variableName] = variableValue
        inputIndex = inputIndex + 1
    if (instruction.startswith("add ")):
        a = instruction.split()[1]
        b = instruction.split()[2]
        if (b.isdigit() or "-" in b):
            res = variables[a] + int(b)
        else:
            res = variables[a] + int(variables[b])
        variables[a] = res
    if (instruction.startswith("mul ")):
        a = instruction.split()[1]
        b = instruction.split()[2]
        if (b.isdigit() or "-" in b):
            res = variables[a] * int(b)
        else:
            res = variables[a] * int(variables[b])
        variables[a] = res
    if (instruction.startswith("div ")):
        a = instruction.split()[1]
        b = instruction.split()[2]
        if (b.isdigit()):
            if (int(b) == 1):
                res = int(variables[a])
            else:
                res = floor(int(variables[a]) / int(b))
        else:
            res = floor(int(variables[a]) / int(variables[b]))
        variables[a] = floor(res)
    if (instruction.startswith("mod ")):
        a = instruction.split()[1]
        b = instruction.split()[2]
        if (b.isdigit()):
            res = variables[a] % int(b)
        else:
            res = variables[a] % int(variables[b])
        variables[a] = res
    if (instruction.startswith("eql ")):
        a = instruction.split()[1]
        b = instruction.split()[2]
        if (b.isdigit()):
            res = variables[a] == int(b)
        else:
            res = variables[a] == int(variables[b])
        variables[a] = int(res)


def runProgram():
    flag = False
    for i in contents:
        if(flag == True and "inp " in i):
            break
        if("inp " in i):
            flag = True
        parseInstruction(i)

runProgram()
print(variables)

# while True:
#     try:
#         runProgram()
#     except (OverflowError):
#         pass
#     if (variables["z"] == 0):
#         print(inputBuffer)
#     inputIndex = 0
#     generateNewInput()
