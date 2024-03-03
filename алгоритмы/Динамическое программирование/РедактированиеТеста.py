def EditDistance(A, B):
    table = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    for k in range(1, len(B) + 1):
        table[0][k] = k
    for l in range(1, len(A) + 1):
        table[l][0] = l
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            insertion = table[i][j - 1] + 1
            deletion = table[i - 1][j] + 1
            match = table[i - 1][j - 1]
            mismatch = table[i - 1][j - 1] + 1
            if A[i - 1] == B[j - 1]:
                table[i][j] = min(insertion, deletion, match)
            else:
                table[i][j] = min(insertion, deletion, mismatch)

    return table[len(A)][len(B)]

a = list(map(str, input().strip()))
b = list(map(str, input().strip()))
c = EditDistance(a, b)
print(c)