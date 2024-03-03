# def merge_sort(list1, list2):
#     sorted_list = []
#     i = 0
#     j = 0
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             sorted_list.append(list1[i])
#             i += 1
#         else:
#             sorted_list.append(list2[j])
#             j += 1
#
#     if i != len(list1):
#         sorted_list.extend(list1[i:])
#     elif j != len(list2):
#         sorted_list.extend(list2[j:])
#
#     return sorted_list
#
# def SelectionSort(a):
#     m = 0
#     for i in range(0, len(a)-1):
#         smallest = i
#         for j in range(i+1, len(a)):
#             if a[j]<a[smallest]:
#                 smallest = j
#         a[i], a[smallest] = a[smallest], a[i]
#     return a
#


def merge_list(a, b):
    c = []
    N = len(a)
    M = len(b)

    i = 0
    j = 0
    while i < N and j < M:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c

def split_and_merge_list(a):
    N1 = len(a) // 2
    a1 = a[:N1]
    a2 = a[N1:]

    if len(a1) > 1:
        a1 = split_and_merge_list(a1)
    if len(a2) > 1:
        a2 = split_and_merge_list(a2)
    return merge_list(a1, a2)


a = list(map(int, input().split()))
a = split_and_merge_list(a)

print(a)

