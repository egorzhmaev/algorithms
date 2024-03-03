# def binary_search(K, q):
#     minIndex = 0
#     maxIndex = len(K) - 1
#     while maxIndex >= minIndex:
#         midIndex = (minIndex + maxIndex) // 2
#         if K[midIndex] == q:
#             return midIndex
#         elif K[midIndex] < q:
#             minIndex = midIndex + 1
#         else:
#             maxIndex = midIndex - 1
#     return 0

# def NaiveBinarySearchWithDuplicates(K, q):
#     minIndex = 0
#     maxIndex = len(K) - 1
#     result = -1
#     while maxIndex >= minIndex:
#         midIndex = (minIndex + maxIndex) // 2
#         if K[midIndex] == q:
#             maxIndex = midIndex - 1
#             result = midIndex
#         elif K[midIndex] < q:
#             minIndex = midIndex + 1
#         else:
#             maxIndex = midIndex - 1
#     return result

def NaiveBinarySearchWithDuplicates(K, q, searchFirst):
    minIndex = 0
    maxIndex = len(K) - 1
    result = -1
    while maxIndex >= minIndex:
        midIndex = (minIndex + maxIndex) // 2
        if K[midIndex] == q:
            result = midIndex
            if searchFirst:
                maxIndex = midIndex - 1
            else:
                minIndex = midIndex + 1
        elif K[midIndex] < q:
            minIndex = midIndex + 1
        else:
            maxIndex = midIndex - 1
    return result


a = int(input())
K = list(map(int, input().split()))
d = int(input())
q = list(map(int, input().split()))
top = []
for i in q:
    count = 0
    first = NaiveBinarySearchWithDuplicates(K, i, True)
    last = NaiveBinarySearchWithDuplicates(K, i, False)
    if first == -1:
        top.append(0)
    else:
        count = last - first + 1
        top.append(count)
print(*top, sep=' ')