def change_nxt(direction, x, y):
    if direction == 0:
        y -= 1
    if direction == 1:
        x += 1
    if direction == 2:
        y += 1
    if direction == 3:
        x -= 1
    return x, y


n, m = map(int, input().split())
room = [[0] * m for _ in range(n)]

for i in range(n):
    line = input()
    for j in range(m):
        if line[j] == '#':
            room[i][j] = 1

y, x = map(int, input().split())
room[y - 1][x - 1] = 2
q = int(input())
queue = input()

count = 1
direction = 0
nxt_x, nxt_y = change_nxt(direction, x, y)

for move in queue:
    if move == 'M' and 0 < nxt_x <= m and 0 < nxt_y <= n:
        if room[nxt_y - 1][nxt_x - 1] == 0:
            x, y = nxt_x, nxt_y
            count += 1
            room[y - 1][x - 1] = 2
        elif room[nxt_y - 1][nxt_x - 1] == 2:
            x, y = nxt_x, nxt_y
    elif move == 'R':
        direction = (direction + 1) % 4
    elif move == 'L':
        direction = (direction - 1) % 4
    nxt_x, nxt_y = change_nxt(direction, x, y)

print(count)