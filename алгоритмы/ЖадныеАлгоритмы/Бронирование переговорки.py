def maxDisjointIntervals(list_):

    list_.sort(key=lambda x: x[1])

    result = 1

    r1 = list_[0][1]

    for i in range(1, len(list_)):
        l1 = list_[i][0]
        r2 = list_[i][1]
        if l1 >= r1:
            result += 1
            r1 = r2

    return result

def read_matrix():
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix

a = read_matrix()
print(maxDisjointIntervals(a))