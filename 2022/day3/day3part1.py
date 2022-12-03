f = open('input.txt', 'r')
content = f.read()

sacks = content.split('\n')
recurItems = []
sum = 0

priorities = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}

for i in range(len(sacks)):
    compOne = sacks[i][:int(len(sacks[i]) / 2)]
    compTwo = sacks[i][int(len(sacks[i]) / 2):]
    recurItems.append(list(set(compOne)&set(compTwo)))
    recurItems = [item for sublist in recurItems for item in sublist]

for i in range(len(recurItems)):
    if(recurItems[i].islower()):
        sum += priorities[recurItems[i]]
    else:
        sum += priorities[recurItems[i].lower()] + 26

print(sum)