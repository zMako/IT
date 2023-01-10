p = int(input())
if p < 1 or p > 10:
    print("error! too many executes!")
    exit()

k = []
d = 0
greatestK = 0
while d < p:
    k.append(int(input()))
    if k[d] < 1:
        print("error! wrong number")
        exit()
    if k[d] > greatestK:
        greatestK = k[d]
    d += 1

fibonacci = [0, 1]
n = 2
while fibonacci[n-1] <= greatestK:
    fibonacci.append(fibonacci[n-1] + fibonacci[n-2])
    n += 1
fibonacci.append(fibonacci[n-1] + fibonacci[n-2])


def findminnumbers(number, previouscount):
    x = 0
    while fibonacci[x] < number:
        x += 1

    if fibonacci[x] == number:
        print(previouscount+1)
    else:
        if (fibonacci[x] - number) < (number - fibonacci[x-1]):
            number = fibonacci[x] - number
            findminnumbers(number, previouscount+1)
        else:
            number = number - fibonacci[x-1]
            findminnumbers(number, previouscount+1)


a = 0

while a < p:
    findminnumbers(k[a], 0)
    a += 1
