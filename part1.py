file = open('input.txt', 'r')
game = []
for line in file:
    line = line.replace(';', ',')
    cutOff = line.index(':')
    line = line[cutOff+2:]
    game.append(list(line.split(', ')))
redActual = 12
greenActual = 13
blueActual = 14
answer = 0
for i in range(len(game)):
    check = 0
    for j in range(len(game[i])):
        value = ''
        for k in game[i][j]:
            if k.isdigit() == True:
                value += k
            else:
                break
        letter = ''
        for l in game[i][j]:
            if l.isalpha() == True:
                letter = l
                break
        if letter == 'b':
            if int(value) <= blueActual:
                check+=1
            else:
                break
        elif letter == 'g':
            if int(value) <= greenActual:
                check+=1
            else:
                break
        elif letter == 'r':
            if int(value) <= redActual:
                check+=1
            else:
                break
    if check == len(game[i]):
        answer += i+1
print(answer)