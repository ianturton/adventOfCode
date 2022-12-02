"""
Find the 3 Elves carrying the most Calories.
How many total Calories is that Elf carrying?

Input is a list of calories one per line with a blank line between elves.
"""
with open("input") as f:
    best = [0, 0, 0]
    lines = f.readlines()
    sum = 0
    for line in lines:
        line = line.strip()
        if line != '':
            sum += int(line)
        else:
            print("before", sum, best)
            for i in range(3):
                if sum > best[i]:
                    # insert the new best and shuffle the rest down
                    best.insert(i, sum)
                    best = best[:3]
                    break
            sum = 0
        print(sum, best)

sum_best = 0
for b in best:
    sum_best += b
print(sum_best)
