def max_pairwise_product(n, m):
    period = PisanoPeriod(m)
    if n <= 1:
        return n
    n=n%period
    F = list(range(0, n+1))
    for i in range(2, n+1):
        F[i] = (F[i - 2] + F[i - 1])
    print(F[n])
    return F[n]

def PisanoPeriod(m):
    current = 0
    next = 1
    period = 0
    while True:
        oldNext = next
        next = (current + next)%m
        current = oldNext
        period = period + 1
        if current == 0 and next == 1:
            return period
    return period


if __name__ == '__main__':
    n, m = map(int, input().split())
    max_pairwise_product(n, m)

#сумма чисел фибоначи n+2