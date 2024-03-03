a, b = map(int, input().split())
arr = list(map(int, input().split()))
def result(b, arr):
    player = arr[b - 1]
    arr.sort()
    count = 0
    ans = 0
    right = len(arr[b:])
    left = len(arr[:b])
    print(right)
    while left:
        if right % 2 == 1:
            left -= 1
        right //= 2
        left //= 2
        ans += 1
    print(ans)

result(b, arr)
# arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
#
# for i in range(1,9):
#     result(i, arr)



