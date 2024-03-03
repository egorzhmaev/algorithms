from functools import lru_cache
def get_longest_increasing_path(matrix):

    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[1] * n for _ in range(m)]

    def dfs(i, j):
        if dp[i][j] == 1:
            dp[i][j] = 1 + max(dfs(i - 1, j) if i > 0 and matrix[i][j] > matrix[i - 1][j] else 0,
                               dfs(i + 1, j) if i < m - 1 and matrix[i][j] > matrix[i + 1][j] else 0,
                               dfs(i, j - 1) if j > 0 and matrix[i][j] > matrix[i][j - 1] else 0,
                               dfs(i, j + 1) if j < n - 1 and matrix[i][j] > matrix[i][j + 1] else 0)
        return dp[i][j]

    return max(dfs(i, j) for i in range(m) for j in range(n))

def read_matrix():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix

matrix = read_matrix()
print(get_longest_increasing_path(matrix))
