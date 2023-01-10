m, p, n = map(int, input().split())

FIRST = m^2
table = []
# SNAKE STRUCTURE: snake[0][0] -> wiersz głowy (pierwszego elementu) snake[0][1] -> kolumna głowy (pierwszego elementu)
# NEEDS INITIALIZATION ^
# SNAKE COORDS STRUCTURE snakeCoords[p][q] -> p (wiersz), q (kolumna) - koordynaty, daje kolor
snake = [[0, 0]]
snakeCoords = []
previousInputs = []
c = 0
while c < m:
    f = 0
    table.append([])
    snakeCoords.append([])
    while f < m:
        table[c].append(0)
        snakeCoords[c].append(-1)
        f += 1
    c += 1

snakeCoords[0][0] = 0

x = 0
while x < p:
    w, k, c = map(int, input().split())
    # warunki

    table[w-1][k-1] = c
    x += 1

checks = []

def movePart(g):
    if list(reversed(previousInputs))[g] == "G":
        snake[g][0] -= 1
        snakeCoords[snake[g][0]][snake[g][1]] = snakeCoords[snake[g][0] + 1][snake[g][1]]
        if g == len(snake) - 1:
            snakeCoords[snake[g][0] + 1][snake[g][1]] = -1
    elif list(reversed(previousInputs))[g] == "D":
        snake[g][0] += 1
        snakeCoords[snake[g][0]][snake[g][1]] = snakeCoords[snake[g][0] - 1][snake[g][1]]
        if g == len(snake) - 1:
            snakeCoords[snake[g][0] - 1][snake[g][1]] = -1
    elif list(reversed(previousInputs))[g] == "L":
        snake[g][1] -= 1
        snakeCoords[snake[g][0]][snake[g][1]] = snakeCoords[snake[g][0]][snake[g][1] + 1]
        if g == len(snake) - 1:
            snakeCoords[snake[g][0]][snake[g][1] + 1] = -1
    elif list(reversed(previousInputs))[g] == "P":
        snake[g][1] += 1
        snakeCoords[snake[g][0]][snake[g][1]] = snakeCoords[snake[g][0]][snake[g][1] - 1]
        if g == len(snake) - 1:
            snakeCoords[snake[g][0]][snake[g][1] - 1] = -1

y = 0
while y < n:
    ins = input()
    if ins == "G":
        previousInputs.append("G")
        if table[snake[0][0] - 1][snake[0][1]] != 0:
            snake.insert(0, [snake[0][0] - 1, snake[0][1]])
            snakeCoords[snake[0][0]][snake[0][1]] = table[snake[0][0]][snake[0][1]]
        else:
            snake[0][0] -= 1
            snakeCoords[snake[0][0]][snake[0][1]] = snakeCoords[snake[0][0] + 1][snake[0][1]]
            g = 1
            while g < len(snake):
                movePart(g)
                g += 1

    elif ins == "D":
        previousInputs.append("D")
        if table[snake[0][0] + 1][snake[0][1]] != 0:
            snake.insert(0, [snake[0][0] + 1, snake[0][1]])
            snakeCoords[snake[0][0]][snake[0][1]] = table[snake[0][0]][snake[0][1]]
        else:
            snake[0][0] += 1
            snakeCoords[snake[0][0]][snake[0][1]] = snakeCoords[snake[0][0] - 1][snake[0][1]]
            g = 1
            while g < len(snake):
                movePart(g)
                g += 1

    elif ins == "L":
        previousInputs.append("L")
        if table[snake[0][0]][snake[0][1] - 1] != 0:
            snake.insert(0, [snake[0][0], snake[0][1] - 1])
            snakeCoords[snake[0][0]][snake[0][1]] = table[snake[0][0]][snake[0][1]]
        else:
            snake[0][1] -= 1
            snakeCoords[snake[0][0]][snake[0][1]] = snakeCoords[snake[0][0]][snake[0][1] + 1]
            g = 1
            while g < len(snake):
                movePart(g)
                g += 1

    elif ins == "P":
        previousInputs.append("P")
        if table[snake[0][0]][snake[0][1] + 1] != 0:
            snake.insert(0, [snake[0][0], snake[0][1] + 1])
            snakeCoords[snake[0][0]][snake[0][1]] = table[snake[0][0]][snake[0][1]]
        else:
            snake[0][1] += 1
            snakeCoords[snake[0][0]][snake[0][1]] = snakeCoords[snake[0][0]][snake[0][1] - 1]
            g = 1
            while g < len(snake):
                movePart(g)
                g += 1

    else:
        z, w, k = ins.split()
        w = int(w)
        k = int(k)
        check = [w-1, k-1]
        if snakeCoords[w-1][k-1] == -1:
            checks.append(-1)
        else:
            checks.append(snakeCoords[w-1][k-1])
    y += 1

for i in checks:
    print(i)