def get_number_of_good_pairs(numbers) -> int:
    result = 0
    first = 0
    nres = 0
    arr = []
    for i in range(len(numbers)):
        i = numbers[i]%200
        arr.append(i)

    while first < 200:
        nres = arr.count(first)
        if nres > 1:
            result += int((nres * (nres - 1) / 2))
        first += 1
    return result

n = int(input())
numbers = list(map(int, input().split()))
print(get_number_of_good_pairs(numbers))

# Статус 200 https://contest.yandex.ru/contest/36783/problems/C/
