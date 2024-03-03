def is_len_right(points, k, length):
    end = points[0] + length
    k -= 1
    for i in range(len(points)):
        if end < points[i]:
            k -= 1
            end = points[i] + length
            if k < 0:
                return False
    return True
def binary_search(k, points):
    if k >= len(points):
        return 0
    min_val = 0
    max_val = points[-1] - points[0]
    while min_val != max_val:
        mid = min_val + (max_val - min_val) // 2
        if is_len_right(points, k, mid):
            max_val = mid
        elif mid == max_val or mid == min_val:
            return max_val
        else:
            min_val = mid
    return max_val

n, k = map(int, input().split())
p = list(map(int, input().split()))
p = sorted(p)
print(binary_search(k, p))

