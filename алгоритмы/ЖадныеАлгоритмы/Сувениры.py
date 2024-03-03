import sys
sys.setrecursionlimit(10000)

def maximum_loot(W, cost):
    if W <= 0:
        return 0
    m = cost.index(min(cost))
    amount = cost[m]
    if W >= amount:
        value = 1
    else:
        return 0
    cost.pop(m)
    return value + maximum_loot(W - amount, cost)

def read_in():
    a, b = map(int, input().split())
    cost = []
    for i in range(a):
        n = int(input())
        cost.append(n)
    return maximum_loot(b, cost)

print(read_in())