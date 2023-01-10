n, k = map(int, input().split())

error = False
if n > 100000 or k >= n or k < 1:
    print("Error! Make sure 1 <= k < n <= 100000")
    error = True
    quit()

nV = n
INF = 999


# Algorithm
def floyd(G):
    global dist
    dist = list(map(lambda p: list(map(lambda q: q, p)), G))

    # Adding vertices individually
    for r in range(nV):
        for p in range(nV):
            for q in range(nV):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])

G = []
s = 0
while s < n:
    G.append([])
    d = 0
    while d < n:
        G[s].append(0)
        d += 1
    s += 1

mk = 0
while mk < n-1:
    a, b, c = map(int, input().split())
    G[a-1][b-1] = c
    G[b-1][a-1] = c
    mk += 1

ad = 0
while ad < n:
    af = 0
    while af < n:
        if G[ad][af] == 0 and ad != af:
            G[ad][af] = INF
        af += 1
    ad += 1

floyd(G)

outputs = 0
previous = [0]
previousTotal = 0
results = []

def getOutput(m):
    global outputs
    global previousTotal
    if outputs == k-1:
        ca = 0
        printTotal = 0
        while ca <= outputs:
            if len(previous) != 0:
                printTotal += 2*(dist[previous[ca]][m-1])
            ca += 1
        total = printTotal + previousTotal
        results.append(total)
        previousTotal = total
        previous.append(m-1)
        return 0
    ca = 0
    printTotal = 0
    while ca <= outputs:
        if len(previous) != 0:
            printTotal += 2*(dist[previous[ca]][m-1])
        ca += 1
    total = printTotal + previousTotal
    results.append(total)
    previousTotal = total
    previous.append(m-1)
    outputs += 1
    getOutput(int(input()))

getOutput(int(input()))

result = 0
while result < len(results):
    print(results[result])
    result += 1
