def neuro_list_merge(list1, list2):
    i = 0
    j = 0
    result = []

    while i < len(list1) and j < len(list2):
        if list[i] < list[j]:
            result.append(list[i])
            i += 1
        else:
            result.append(list[j])
            j += 1

    if i != len(list1):
        result.extend(list1[i:])
    elif j != len(list2):
        result.extend(list1[i:])

    return result

# Списки состоят из строик типа, списки отсортированы
# 1692458250 neurodivergence.altitude.z0 328134

# Если на входе n-ое количество списков? Очередь с приоритетами. Как?
result = []
list1 = ['1692458251 neurodivergence.altitude.z0 328134','1692458253 neurodivergence.altitude.z0 328134','1692458255 neurodivergence.altitude.z0 328134']
list2 = ['1692458252 neurodivergence.altitude.z0 328134','1692458251 neurodivergence.altitude.z0 328135','1692458256 neurodivergence.altitude.z0 328134']
result = list1 + list2
result.sort()
print(result)