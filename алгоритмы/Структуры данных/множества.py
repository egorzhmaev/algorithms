def is_one_away(word1, word2):
    m1 = 0
    for l in range(0, len(word1)):
        if word1[l] == word2[l]:
            continue
        else:
            m1 += 1
    return m1 == 1


n = int(input())
matrix = []
for i in range(n):
    matrix.append(str(input()))

result = 0

for j in range(0, n-1):
    for k in range(j+1, n):
        if is_one_away(matrix[j], matrix[k]):
            result += 1

print(result)
