file = open('input.txt', 'r')
game = []
for line in file:
    line = line.replace(';', ',')
    cutOff = line.index(':')
    line = line[cutOff+2:]
    game.append(list(line.split(', ')))
answer = 0
for i in range(len(game)):
    lowestRed = 0
    lowestGreen = 0
    lowestBlue = 0
    for j in range(len(game[i])):
        ###Gets the first numbers
        value = ''
        for k in game[i][j]:
            if k.isdigit() == True:
                value += k
            else:
                value = int(value)
                break
        ###Gets the first letter
        letter = ''
        for l in game[i][j]:
            if l.isalpha() == True:
                letter = l
                break
        
        if letter == 'r':
            if lowestRed < int(value):
                lowestRed = int(value)
        if letter == 'b':
            if lowestBlue < int(value):
                lowestBlue = int(value)
        if letter == 'g':
            if lowestGreen < int(value):
                lowestGreen = int(value)
    print(lowestBlue,lowestGreen,lowestRed)
    answer += lowestBlue*lowestGreen*lowestRed
print(answer)