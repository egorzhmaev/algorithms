def GCD(a, b):
    if a == 0 or b == 0:
        return max(a,b)
    return GCD(b,a%b)

a, b = map(int, input().split())
print(GCD(a,b))


def GCD(a, b):
    if a == 0 or b == 0:
        return max(a,b)
    return GCD(b,a%b)

def LCM(a,b,c):
    return ((a*b)//c)

a, b = map(int, input().split())
c = GCD(a,b)
print(LCM(a,b,c))

n = int(input())
a ,b = 1, 0
while True:
    if (a+b) <= n:
        if a>b:
            b += a
        else:
            a += b
    else:
        break
print(min(a,b), max(a,b))