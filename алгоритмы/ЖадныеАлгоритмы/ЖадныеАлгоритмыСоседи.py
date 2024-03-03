def segments_cover():
    m = int(input())
    segments = []
    for i in range(m):
        segments.append(list(map(int, input().split())))

    points = set()
    while segments:
        j = 0
        b = len(segments)
        r_m = min(segment[1] for segment in segments)
        points.add(r_m)
        while j < b:
            nume = segments[j]
            if nume[0]<=r_m<=nume[1]:
                segments.pop(j)
                b -= 1
            else:
                j += 1
    print(len(points))
    print(*points, sep=' ')

segments_cover()


#Задача про отрезки
# def segments_cover():
#     n, l = map(int, input().split())
#     segments = list(set(map(int, input().split())))
#     segments.sort()
#     points = 1
#     first = min(segments)+l
#     for i in range(0, len(segments)):
#         if segments[i] > first:
#             first = segments[i]+l
#             points += 1
#     print(points)
#
# segments_cover()

#Задача про отрезки №2
# def segments_cover():
#     n, l = map(int, input().split())
#     segments = list(map(int, input().split()))
#     if l >= len(segments):
#         print(0)
#     else:
#         segments = list(set(segments))
#         segments.sort()
#         new_seg = []
#         for i in range(0, len(segments)-1):
#             new_seg.append(segments[i+1]-segments[i])
#         new_seg.sort()
#         l -= 1
#         if l == 0:
#             print (sum(new_seg))
#         else:
#             new_seg = new_seg[:-l]
#             print(sum(new_seg))
#
# segments_cover()




