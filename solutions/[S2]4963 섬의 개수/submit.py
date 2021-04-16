# [S2]4963 섬의 개수
# https://www.acmicpc.net/problem/4963

import sys
from collections import deque
input = sys.stdin.readline

dx = [0,1,0,-1,1,1,-1,-1]
dy = [1,0,-1,0,1,-1,1,-1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    que = deque()
    island = 0
    for a in range(h):
        for b in range(w):
            if arr[a][b] == 1 and visited[a][b] == False:
                que.append((a,b))
                visited[a][b] = True
                island += 1

            while que:
                x, y = que.popleft()
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx == h or ny == w:
                        continue
                    if arr[nx][ny] == 1 and visited[nx][ny] == False:
                        que.append((nx,ny))
                        visited[nx][ny] = True

    print(island)