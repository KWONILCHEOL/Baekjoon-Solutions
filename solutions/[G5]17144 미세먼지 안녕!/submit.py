# [G5]17144 미세먼지 안녕!
# https://www.acmicpc.net/problem/17144

import sys
from collections import deque
input = sys.stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def move(a, b):
    if a <= air:
        if (a, b) == (air, c - 1):
            a -= 1
        elif (a, b) == (0, c - 1):
            b -= 1
        elif (a, b) == (0, 0):
            a += 1
        else:
            if a == air:
                b += 1
            elif b == c - 1:
                a -= 1
            elif a == 0:
                b -= 1
            elif b == 0:
                a += 1
                if a == air:
                    return -1, -1
    elif a > air:
        if (a, b) == (r - 1, 0):
            a -= 1
        elif (a, b) == (r - 1, c - 1):
            b -= 1
        elif (a, b) == (air + 1, c - 1):
            a += 1
        else:
            if a == air + 1:
                b += 1
            elif b == c - 1:
                a += 1
            elif a == r - 1:
                b -= 1
            elif b == 0:
                a -= 1
                if a == air + 1:
                    return -1, -1

    return a, b

r, c, t = map(int,input().split())
A = [list(map(int, input().split())) for _ in range(r)]
que = deque()
air = 0
for i in range(r):
    if A[i][0] == -1:
        air = i
        break

for i in range(r):
    for j in range(c):
        if A[i][j] > 0:
            que.append((i,j,A[i][j]))

for _ in range(t):
    A = [[0] * c for _ in range(r)]
    temp = set()
    length = len(que)
    # 확산
    for _ in range(length):
        x,y,v = que.popleft()
        cnt = 0
        for i in range(4):
            if v < 5:
                break
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx == r or ny == c:
                continue
            if ny == 0 and (nx == air or nx == (air + 1)):
                continue

            A[nx][ny] += v//5
            temp.add((nx,ny))
            cnt += 1

        A[x][y] += v - ((v // 5) * cnt)
        temp.add((x,y))

    # 이동
    A2 = [[0] * c for _ in range(r)]
    for x,y in temp:
        nx, ny = move(x,y)
        if (nx, ny) == (-1,-1):
            continue
        A2[nx][ny] = A[x][y]
        que.append((nx,ny,A2[nx][ny]))

answer = 0
for item in que:
    answer += item[2]
print(answer)