result = []
def HanoiTowers(n, fromPeg, toPeg):
    if n == 1:
        result.append([fromPeg, toPeg])
        return
    unusedPeg = 6 - fromPeg - toPeg
    HanoiTowers(n-1, fromPeg, unusedPeg)
    result.append([fromPeg, toPeg])
    HanoiTowers(n-1, unusedPeg, toPeg)
    return result

a = int(input())
HanoiTowers(a, 1, 3)
print (len(result))
for i in result:
    print(*i, sep=' ')