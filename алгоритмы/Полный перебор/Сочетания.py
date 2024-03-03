a, b = map(int, input().split())

def fact(c):
    fact = 1
    for x in range(1, c+1):
        fact = fact*x
    return fact

result = fact(a)/(fact(b)*fact(a-b))

print(int(result))