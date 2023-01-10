with open('aoc1.txt') as f:
    lines = f.readlines()

elfCalories = []
count = 0

for line in lines:
    if line.strip():
        count += int(line)
    else:
        elfCalories.append(count)
        count = 0

elfCalories = sorted(elfCalories)

print(f"1st Answer: {elfCalories[len(elfCalories)-1]}")
print(f"2nd Answer: {elfCalories[len(elfCalories)-3] + elfCalories[len(elfCalories)-2] + elfCalories[len(elfCalories)-1]}")