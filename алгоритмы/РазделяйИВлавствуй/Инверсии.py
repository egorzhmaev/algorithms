
def Merge(LeftHalf, RightHalf, inversions):
    SortedList = []
    while LeftHalf and RightHalf:
        l = 0
        r = 0
        if LeftHalf[l] <= RightHalf[r]:
            SortedList.append(LeftHalf[l])
            LeftHalf.pop(l)
        else:
            SortedList.append(RightHalf[r])
            RightHalf.pop(r)
            inversions = inversions + len(LeftHalf)
    SortedList += LeftHalf + RightHalf
    return SortedList, inversions

def CountInversions(List, inv):
    if len(List) <= 1:
        return 0, 0
    mid = len(List)//2
    LeftHalf = List[:mid]
    RightHalf = List[mid:]
    if len(LeftHalf) > 1:
        LeftHalf, inv = CountInversions(LeftHalf, inv)
    if len(RightHalf) > 1:
        RightHalf, inv = CountInversions(RightHalf, inv)
    return Merge(LeftHalf, RightHalf, inv)

a = int(input())
b = list(map(int, input().split()))
inversions = 0
c, d = CountInversions(b, inversions)
print(d)

