n = int(input())
matrix = []
stack1 = []
for i in range(n):
    m = list(map(int, input().split()))
    matrix.append(m)

for j in matrix:
    if j[0] == 1:
        stack1.append(j[1])
        print(stack1[0])
    if j[0] == 2:
        if stack1:
            stack1.pop(0)
            if stack1:
                print(stack1[0])
            else:
                print(-1)
        else:
            print(-1)