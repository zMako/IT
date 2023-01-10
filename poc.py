n, m, k = map(int, input().split())

error = False
if n < m:
    print("Error! Make sure n >= m")
    error = True
    quit()

bajtek = list(map(int, input().split()))
if len(bajtek) != n:
    print("Error! Wrong amount of numbers provided by the Bajtek's input!")
    error = True

bitek = list(map(int, input().split()))
if len(bitek) != m:
    print("Error! Wrong amount of numbers provided by the Bitek's input!")
    error = True

if error == True:
    quit()

if all(i > k for i in bajtek):
    print("Error! Your mapping input for bajtek contains too high values!")

if all(i > k for i in bitek):
    print("Error! Your mapping input for bajtek contains too high values!")

toppossibilities = []

x = m-1
y = n-1

while len(toppossibilities) < m:
    if bitek[x] == bajtek[y]:
        toppossibilities.append(y+1)
        x -= 1
        y -= 1
    else:
        y -= 1

lowpossibilities = []

a = 0
b = 0

while len(lowpossibilities) < m:
    if bitek[a] == bajtek[b]:
        lowpossibilities.append(b+1)
        a += 1
        b += 1
    else:
        b += 1

possibilities = []
possible = []
impossible = []
extra = []

# Formatowanie wyjscia:
c = 0
while c < n:
    if c+1 in lowpossibilities:
        possible.append(bajtek[c])
    if c+1 in toppossibilities:
        impossible.append(bajtek[c])
    if bajtek[c] in possible and bajtek[c] not in impossible:
        extra.append(c+1)
    c += 1

possibilities = sorted(set(lowpossibilities + extra + toppossibilities))

output = []
s = 0
v = 1
while s < len(possibilities):
    if possibilities[s] == v:
        output.append(1)
        s += 1
        v += 1
    else:
        v += 1
        output.append(0)

if possibilities[-1] != n:
    g = n - possibilities[-1]
    f = 0
    while f < g:
        output.append(0)
        f += 1

print(*output, sep=' ')