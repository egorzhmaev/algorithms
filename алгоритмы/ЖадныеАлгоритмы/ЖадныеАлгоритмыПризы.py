a = int(input())
result = 0
for i in range(1, a+1):
    if a < ((i*(i+1))/2):
        result = i-1
        break
print(result)
