# -*- coding:utf-8 -*-
import math

def distance(p1, p2):
    x = math.fabs(p1[0] - p2[0])
    y = math.fabs(p1[1] - p2[1])
    return math.sqrt(x*x + y*y)

def get_closest_distance(points, l, r):
    if r - l == 1:                          # Только две точки решаются напрямую
        return [distance(points[l], points[r]), l, r]
    elif r - l == 2:                          # Используйте метод сравнения для трех точек
        d1 = distance(points[l], points[l+1])
        d2 = distance(points[l+1], points[r])
        d3 = distance(points[l], points[r])
        if d1 <= d2 and d1 <= d3:
            return [d1, l, l+1]
        elif d2 <= d1 and d2 <= d3:
            return [d2, l+1, r]
        else:
            return [d3, l, r]
# Используйте метод «разделяй и властвуй»
    m = l + (r - l) // 2
    result = min(get_closest_distance(points, l, m), get_closest_distance(points, m+1, r))
    #midle_x = points[m][0]
    #close_points = list(filter(lambda p: abs(p[0]-midle_x) < result[0], points[l:r]))
    i = m
    j = m
    while i >= l:  # Найдите значение слева
        if points[m][0] - points[i][0] < result[0]:
            i -= 1
        else:
            break
    while j <= r:  # Найдите значение справа
        if points[j][0] - points[m][0] < result[0]:
            j += 1
        else:
            break
    if i < m:  # Если нет совпадающей точки слева от m, я останусь в это время на m. Если есть, то i будет на один бит перед самой левой точкой, поэтому +1
        i += 1
    result3 = [65535, 0, 0]
    for a in range(i, m + 1):  # range () Слева закрыта, а справа открыта, нам нужна точка m как левая точка
        for b in range(m + 1,j):  # j - позиция крайней правой точки справа, которая удовлетворяет условию +1, из-за диапазона j не включается
            d0 = distance(points[a], points[b])
            if d0 < result3[0]:
                result3 = [d0, a, b]
    # for i in range(len(close_points)):                     # range () Слева закрыта, а справа открыта, нам нужна точка m как левая точка
    #     for j in range(i-1, 0, -1):                 # j - позиция крайней правой точки справа, которая удовлетворяет условию +1, из-за диапазона j не включается
    #         d0 = distance(points[i], points[j])
    #         if d0 < result[0]:
    #             result3 = [d0, i, j]
    return (min(result, result3))

def read_matrix():
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix

p = read_matrix()
p = sorted(p)
result_new = get_closest_distance(p, 0, len(p)-1)
print(format(result_new[0], '.6f'))

