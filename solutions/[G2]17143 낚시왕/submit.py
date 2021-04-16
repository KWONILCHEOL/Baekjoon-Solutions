# [G2]17143 낚시왕
# https://www.acmicpc.net/problem/17143

import sys
from collections import deque
input = sys.stdin.readline

def fish():
    for i in range(1, R+1):
        if arr[i][j] != 0:
            q.remove((i,j,arr[i][j][0],arr[i][j][1],arr[i][j][2]))
            ret = arr[i][j][2]
            arr[i][j] = 0
            return ret
    return 0

def move():
    length = len(q)

    for r,c,s,d,z in q:
        arr[r][c] = 0

    for _ in range(length):
        r, c, s, d, z = q.popleft()

        if d == 1:  #위
            r -= s
            if r < 1:
                r = -r + 2
                d = 2
            if r > R:
                r = R * 2 - r #r - ((r-R)*2)
                d = 1
        elif d == 2:#아래
            r += s
            if r > R:
                r = R * 2 - r
                d = 1
            if r < 1:
                r = -r + 2
                d = 2
        elif d == 3:#우
            c += s
            if c > C:
                c = C * 2 - c
                d = 4
            if c < 1:
                c = -c + 2
                d = 3
        elif d == 4:#좌
            c -= s
            if c < 1:
                c = -c + 2
                d = 3
            if c > C:
                c = C * 2 - c
                d = 4

        if arr[r][c] != 0:
            if arr[r][c][2] < z:
                q.remove((r,c,arr[r][c][0],arr[r][c][1],arr[r][c][2]))
                arr[r][c] = (s,d,z)
                q.append((r,c,s,d,z))
        else:
            arr[r][c] = (s,d,z)
            q.append((r, c, s, d, z))

R, C, m = map(int,input().split())
arr = [[0] * (C + 1) for _ in range(R + 1)]
answer = 0

q = deque()
for i in range(m):
    r, c, s, d, z = map(int, input().split())   #위(1) 아래(2) 우(3) 좌(4)
    if d < 3:
        if s >= (R -1)  * 2:
            s %= ((R - 1) * 2)
    elif d > 2:
        if s >= (C - 1) * 2:
            s %= ((C - 1) * 2)
    arr[r][c] = (s,d,z)
    q.append((r,c,s,d,z))

for j in range(1, C + 1):
    answer += fish()
    move()
print(answer)