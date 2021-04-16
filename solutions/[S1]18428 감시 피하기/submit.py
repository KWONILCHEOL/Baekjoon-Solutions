# [S1]18428 감시 피하기
# https://www.acmicpc.net/problem/18428

import sys
input = sys.stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def check():
    for x,y in T:
        for i in range(4):
            nx, ny = x, y
            while True:
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or ny < 0 or nx == n or ny == n or A[nx][ny] == 'O':
                    break
                if A[nx][ny] == 'S':
                    return False
    return True

def go(cur, cnt):
    if X_Size - cur + cnt < 3:
        return

    if cnt == 3:
        if check():
            print("YES")
            sys.exit()
        return

    if cur == X_Size:
        return

    x,y = X[cur]
    A[x][y] = 'O'
    go(cur + 1, cnt + 1)
    A[x][y] = 'X'
    go(cur + 1, cnt)

n = int(input())
A = [list(input().rstrip().split()) for _ in range(n)]
X, T = [], []

for i in range(n):
    for j in range(n):
        if A[i][j] == 'X':
            X.append((i,j))
        if A[i][j] == 'T':
            T.append((i,j))

X_Size = len(X)
go(0, 0)
print("NO")