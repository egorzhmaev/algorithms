n, m = map(int, input().split())
matrix = []
matrix_one = [[0 for _ in range(n)] for _ in range(n)]
matrix_two = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    k = list(map(int, input().split()))
    k.pop(0)
    matrix.append(k)

def oneGraph(twoGraph, route):
    for i in range(0, len(route) - 1):
        for j in range(i + 1, len(route)):
            oneRoute = route[i]
            twoRoute = route[j]
            twoGraph[oneRoute - 1][twoRoute - 1] = 1
            twoGraph[twoRoute - 1][oneRoute - 1] = 1

for i in matrix:
    oneGraph(matrix_two, i)
    for j in range(len(i)):
        if j == 0:
            matrix_one[i[j]-1][i[j+1]-1] = 1
        elif j == len(i)-1:
            matrix_one[i[j] - 1][i[j - 1] - 1] = 1
        else:
            matrix_one[i[j] - 1][i[j + 1] - 1] = 1
            matrix_one[i[j] - 1][i[j - 1] - 1] = 1


for i in matrix_one:
    print(*i, sep=' ')
for i in matrix_two:
    print(*i, sep=' ')


