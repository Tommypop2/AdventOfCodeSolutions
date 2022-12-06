# Map of reponse to play
winMap = {"A": "C", "B": "A", "C": "B"}
lossMap = {}
for i in winMap.keys():
    lossMap[winMap[i]] = i

def getResponse(outcome, play):
    if (outcome == 0): #Loss outcome
        response = winMap[play]
    elif(outcome == 1): #Draw outcome
        response = play
    else: #Win outcome
        response = lossMap[play]
    return response

def getScore(play, response):
    outcome = 0
    if (winMap[response] == play):  # Win condition
        outcome = 6
    elif (response == play):  # Draw condition
        outcome = 3
    else:  # Loss condition
        outcome = 0
    return (ord(response) - 64) + outcome


with open("input.txt", "r") as f:
    lines = f.readlines()
score = 0
for line in lines:
    play, wantedOutcome = line.strip().split(" ")
    wantedOutcome = ord(wantedOutcome) - 88
    response = getResponse(wantedOutcome, play)
    score += getScore(play, response)
print(score)
