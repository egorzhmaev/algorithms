from typing import List
def findLongestFromACell(i, j, mat, dp):
    n, m = len(mat), len(mat[0])

    if i < 0 or i >= n or j < 0 or j >= m:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    x, y, z, w = -1, -1, -1, -1

    if j < m - 1 and mat[i][j] < mat[i][j + 1]:
        x = 1 + findLongestFromACell(i, j + 1, mat, dp)

    if j > 0 and mat[i][j] < mat[i][j - 1]:
        y = 1 + findLongestFromACell(i, j - 1, mat, dp)

    if i > 0 and mat[i][j] < mat[i - 1][j]:
        z = 1 + findLongestFromACell(i - 1, j, mat, dp)

    if i < n - 1 and mat[i][j] < mat[i + 1][j]:
        w = 1 + findLongestFromACell(i + 1, j, mat, dp)

    dp[i][j] = max(x, max(y, max(z, max(w, 1))))
    return dp[i][j]


def get_longest_increasing_path(mat: List[List[int]]) -> int:
    result = 1
    n, m = len(mat), len(mat[0])
    dp = [[-1 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                findLongestFromACell(i, j, mat, dp)

            result = max(result, dp[i][j])
    return result

def read_matrix() -> List[List[int]]:
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix

mat = read_matrix()
print(get_longest_increasing_path(mat))
