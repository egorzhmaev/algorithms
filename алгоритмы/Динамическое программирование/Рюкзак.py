def knapsack(w, W):
    pack = [[False] * (len(w) + 1) for _ in range(W + 1)]
    pack[0][0] = True
    result = 0
    for i in range(1, len(w) + 1):
        for j in range(W + 1):
            if w[i - 1] > j:
                pack[j][i] = pack[j][i - 1]
            else:
                pack[j][i] = pack[j][i - 1] or pack[j - w[i - 1]][i - 1]
            if pack[j][i]:
                result = j
    return result

a, b = map(int, input().split())
w = list(map(int, input().split()))
print(knapsack(w, a))
