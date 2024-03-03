n, k = map(int, input().split())

def fact(c):
    fact = 1
    for x in range(1, c+1):
        fact = fact*x
    return fact

result = fact(k+n-1)/(fact(n-1)*fact(k))

print(int(result))