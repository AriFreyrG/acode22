with open('d1.in.txt') as f:
    lines = f.readlines()

mostCalories = 0
tempCalories = 0

howManyElves = lines.count("\n") +1
elves = [0] * howManyElves
currentElf = 0

for i in range(len(lines)):
    
    if lines[i] != "\n":
        lineCal = lines[i].strip("\n")
        elves[currentElf] += int(lineCal)
    elif lines[i] == "\n":
        
        currentElf += 1
        
    
sortedElves = sorted(elves)
lastthree = sum(sortedElves[-3:])

print(lastthree)