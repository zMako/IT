with open('aoc2.txt') as f:
    lines = f.readlines()

winsWith = {
    "X": "C",
    "Y": "A",
    "Z": "B"
}

losesTo = {
    "X": "B",
    "Y": "C",
    "Z": "A"
}

choiceScore = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

totalScore = 0

for line in lines:
    if line.split()[0] == winsWith[line.split()[1]]: # we won
        totalScore += 6
    elif line.split()[0] == losesTo[line.split()[1]]: # we lost
        totalScore += 0
    else: # draw
        totalScore += 3
    totalScore += choiceScore[line.split()[1]]

print(f"1st Answer: {totalScore}")

# SECOND PART
win = {
    "A": 2,
    "B": 3,
    "C": 1
}

loss = {
    "A": 3,
    "B": 1,
    "C": 2
}

draw = {
    "A": 1,
    "B": 2,
    "C": 3
}

totalScore2 = 0

for line in lines:
    if line.split()[1] == "X": # we need to lose
        totalScore2 += loss[line.split()[0]]
    elif line.split()[1] == "Y": # we need to draw
        totalScore2 += draw[line.split()[0]] + 3
    else: # we need to win
        totalScore2 += win[line.split()[0]] + 6

print(f"2nd Answer: {totalScore2}")