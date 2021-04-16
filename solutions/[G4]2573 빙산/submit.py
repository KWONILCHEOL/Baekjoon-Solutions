# [G4]2573 빙산
# https://www.acmicpc.net/problem/2573

import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
ice = [[x,y,0] for x in range(n) for y in range(m) if arr[x][y] != 0]
time = 0
while True:
    time += 1
    #녹일 빙산 계산
    for i in range(len(ice)):
        x, y, v = ice[i]
        cnt = 0
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or ny < 0 or nx == n or ny == m:
                continue
            if arr[nx][ny] == 0:
                cnt += 1
        cnt = arr[x][y] - cnt
        ice[i] = [x,y,cnt]

    #녹이기
    for i in range(len(ice)-1,-1,-1):
        x, y, v = ice[i]
        if v <= 0:
            arr[x][y] = 0
            ice.remove(ice[i])
        else:
            arr[x][y] = v

    #확인
    if len(ice) == 0:
        time = 0
        break
    ice2 = deepcopy(ice)
    visited = [[False] * m for _ in range(n)]
    que = deque()
    que.append((ice2[0][0], ice2[0][1]))
    visited[que[0][0]][que[0][1]] = True
    cnt = 0
    while que:
        x,y = que.pop()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx == n or ny == m or visited[nx][ny]:
                continue
            if arr[nx][ny] > 0:
                que.append((nx,ny))
                visited[nx][ny] = True

    if len(ice) != cnt:
        break

print(time)