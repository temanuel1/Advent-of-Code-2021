safe = 0

with open('/Users/tyleremanuel/Documents/Advent-of-Code/2024/day2/input.txt', 'r') as file:
    for line in file:
        diffs = []
        numbers = list(map(int, line.strip().split()))
        for i in range(len(numbers) - 1):
            diffs.append(numbers[i+1] - numbers[i])
        if all(3 >= a >= 1 for a in diffs):
            safe += 1
        elif (all(-1 >= b >= -3 for b in diffs)):
            safe += 1

print(safe)