def reversed1(variable):
    res=''
    for i in range(len(variable)-1,-1,-1):
        res+=variable[i]
    return res

n = reversed1(input())
print(n)


def reversed3(variable):
    if len(variable) == 1:
        return variable
    return variable[-1] + reversed3(variable[:-1])

n = reversed3(input())
print(n)


def reverse_list(arr):
    left = 0
    right = len(arr) - 1
    while (left < right):
        # Swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(arr))