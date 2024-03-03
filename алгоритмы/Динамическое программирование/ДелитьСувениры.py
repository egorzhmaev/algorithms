def split(v):
    if sum(v) % 3 != 0:
        return print(0)
    V = sum(v) // 3
    n = len(v)
    split = [[[False for _ in range(V+1)] for _ in range(V+1)] for _ in range(n+1)]
    split[0][0][0] = True
    for i in range(1, n+1):
        for s1 in range(V+1):
            for s2 in range(V+1):
                split[i][s1][s2] = split[i-1][s1][s2]
                if s1 >= v[i-1]:
                    split[i][s1][s2] = split[i][s1][s2] or split[i-1][s1-v[i-1]][s2]
                if s2 >= v[i-1]:
                    split[i][s1][s2] = split[i][s1][s2] or split[i-1][s1][s2-v[i-1]]
    if split[n][V][V]:
        print(1)
    else:
        print(0)

a = int(input())
b = list(map(int, input().split()))
split(b)