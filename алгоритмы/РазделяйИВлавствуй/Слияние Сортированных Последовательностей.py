def read_matrix():
    num = int(input())
    matrix = []
    mat = []
    if num == 1:
        n = int(input())
        arr = list(map(int, input().split()))
        return print(*sorted(arr), sep=' ')
    else:
        for i in range(num):
            n = int(input())
            matrix.append(list(map(int, input().split())))
        for j in range(0, len(matrix)):
            mat = mat + matrix[j]
        return print(*sorted(mat), sep=' ')

read_matrix()