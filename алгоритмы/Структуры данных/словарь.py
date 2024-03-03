n = int(input())
matrix = []
dict1 = {}
for i in range(n):
    m = list(map(int, input().split()))
    matrix.append(m)

for j in matrix:
    if j[0] == 1:
        if j[1] not in dict1:
            dict1.setdefault(j[1], j[2])
        else:
            dict1[j[1]]=j[2]
    if j[0] == 2:
        if j[1] in dict1:
            print(dict1[j[1]])
        else:
            print(-1)