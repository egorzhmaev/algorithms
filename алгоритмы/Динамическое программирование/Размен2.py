def change(money):
    table = [float('inf')] * (money + 1)
    table[0] = 0
    for m in range(1, money + 1):
        for c in [1, 3, 4]:
            if c <= m:
                table[m] = min(table[m], 1 + table[m - c])
                print(table)
    return table[money]

a = int(input())
answer = change(a)
print(answer)