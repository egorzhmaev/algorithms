a, b = map(int, input().split())

def Rocks(n, m):
    R = [[None] * (m+1) for _ in range(n+1)]
    R[0][0] = 'Loose'
    R[1][0] = 'Win'
    R[0][1] = 'Win'
    for i in range(2, n+1):
        if R[i-1][0] == 'Win' and R[i-2][0] == 'Win':
            R[i][0] = 'Loose'
        else:
            R[i][0] = 'Win'
    for j in range(2, m+1):
        if R[0][j-1] == 'Win' and R[0][j-2] == 'Win':
            R[0][j] = 'Loose'
        else:
            R[0][j] = 'Win'
    for i in range(1, n+1):
        for j in range(1, m+1):
            if R[i][j-1] == 'Win' and R[i-1][j] == 'Win':
                R[i][j] = 'Loose'
            else:
                R[i][j] = 'Win'

    return R[n][m]

print(Rocks(a, b))

# def FastRocks(n, m):
#     if n % 2== 0 and m % 2 == 0:
#         print('Loose')
#     else:
#         print('Win')
#
# FastRocks(a, b)
