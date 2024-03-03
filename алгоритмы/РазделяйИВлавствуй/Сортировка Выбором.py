def SelectionSort(a):
    m = 0
    for i in range(0, len(a)-1):
        smallest = i
        for j in range(i+1, len(a)):
            if a[j]<a[smallest]:
                smallest = j
        a[i], a[smallest] = a[smallest], a[i]
    return print(*a, sep=' ')

num = int(input())
arr = list(map(int, input().split()))

SelectionSort(arr)