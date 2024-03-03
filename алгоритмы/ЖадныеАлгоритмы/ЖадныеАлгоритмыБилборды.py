def solution():
    n, k, w = map(int, input().split())
    if n * k * w == 0:
        return 0
    adv = []
    for _ in range(k):
        adv.append([int(i) for i in input().split()])

    boards = w * n
    adv = sorted(adv, key=lambda x: (x[0], x[1]))

    result = 0
    while boards > 0 and adv:
        c_i, w_i = adv.pop()
        time = min(w_i, w, boards)
        result += c_i * time
        boards -= time
    return result

print(solution())
