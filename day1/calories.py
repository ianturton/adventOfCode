"""
Find the Elf carrying the most Calories.
How many total Calories is that Elf carrying?

Input is a list of calories one per line with a blank line between elves.
"""
with open("input") as f:
    best = 0
    lines = f.readlines()
    sum = 0
    for line in lines:
        line = line.strip()
        print("*"+line+"*")
        if line != '':
            sum += int(line)
        else:
            if sum > best:
                best = sum
            sum = 0
        print(sum, best)

print(best)
