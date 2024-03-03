def LCS(A, B, C):
    table = [[[0 for k in range(len(C) + 1)] for j in range(len(B) + 1)] for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            for k in range(1, len(C) + 1):
                one = table[i - 1][j][k]
                two = table[i][j - 1][k]
                three = table[i][j][k - 1]
                table[i][j][k] = max(one, two, three)
                if A[i - 1] == B[j - 1] == C[k - 1]:
                    table[i][j][k] = max(table[i][j][k], table[i - 1][j - 1][k - 1] + 1)
    return table[len(A)][len(B)][len(C)]

n = int(input())
a = list(map(str, input().split()))
m = int(input())
b = list(map(str, input().split()))
v = int(input())
c = list(map(str, input().split()))

print(LCS(a,b,c))