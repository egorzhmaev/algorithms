a = int(input())
b = list(map(int, input().split()))
nums = {}
for i in b:
    nums.setdefault(i, 0)
    nums[i] += 1
count = 0
for i in nums:
    if nums[i] > a/4:
        count += 1

if count >= 3:
    print(1)
else:
    print(0)