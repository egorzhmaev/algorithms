def largest_substring(s):
    lsub = 0
    i = j = 0
    while i < len(s)-1:
        curr = ""
        while s[j] not in curr and j < len(s)-1:
            curr += s[j]
            j += 1
            lsub = max(lsub, len(curr))
        i = j
    return lsub

print(largest_substring(input()))
