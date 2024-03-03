n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr1 = arr[0:m]
k = min(arr1)
for i in range(m, len(arr)):
    arr1.append(arr[i])
    arr1.pop(0)
    k += min(arr1)

print(k)
