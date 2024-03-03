import sys
sys.setrecursionlimit(10000)

def maximum_loot(W, weight, cost, most_exp):
    if W == 0 or not weight:
        return 0
    m = most_exp.index(max(most_exp))
    amount = min(weight[m], W)
    value = (cost[m] / weight[m]) * amount
    weight.pop(m)
    cost.pop(m)
    most_exp.pop(m)
    return value + maximum_loot(W - amount, weight, cost, most_exp)

def read_in():
    a, b = map(int, input().split())
    weig = []
    cost = []
    most_exp = []
    for i in range(a):
        m, n = map(int, input().split())
        cost.append(m)
        weig.append(n)
    for i in range(a):
        most_exp.append(cost[i] / weig[i])
    return maximum_loot(b, weig, cost, most_exp)


print(format(read_in(), '.3f'))

