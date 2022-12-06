# Map of reponse to play
winMap = {"A": "C", "B": "A", "C": "B"}


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
    play, response = line.strip().split(" ")
    response = chr(ord(response) - 23)
    score += getScore(play, response)
print(score)
