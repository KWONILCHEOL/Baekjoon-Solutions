# [G5]2636 치즈
# https://www.acmicpc.net/problem/2636

import sys
import copy
from collections import deque
input = sys.stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
chz1, chz2 = deque(), deque()    #녹을 치즈, 다음에 녹을 치즈

for i in range(1, n-2):
    if arr[i][0] == 0:
        chz1.append((i,0))
    if arr[i][m-1] == 0:
        chz1.append((i, m-1))
    visited[i][0] = True
    visited[i][m - 1] = True

for j in range(1, m-2):
    if arr[0][j] == 0:
        chz1.append((0,j))
    if arr[n-1][j] == 0:
        chz1.append((n-1,j))
    visited[0][j] = True
    visited[n-1][j] = True

cheese_n = sum(sum(x) for x in arr)
if cheese_n == 0:
    print(1,1,sep='\n')
    sys.exit()

time = 0
while True:
    time += 1
    while chz1:
        x,y = chz1.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx == n or ny == m or visited[nx][ny]:
                continue
            if arr[nx][ny] == 0:
                chz1.append((nx, ny))
            elif arr[nx][ny] == 1:
                chz2.append((nx, ny))
            visited[nx][ny] = True

    chz1 = copy.deepcopy(chz2)
    chz2.clear()

    if cheese_n == len(chz1):
        break
    cheese_n -= len(chz1)

print(time, cheese_n, sep='\n', end='')
