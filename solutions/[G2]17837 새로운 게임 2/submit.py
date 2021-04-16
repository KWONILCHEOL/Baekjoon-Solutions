# [G2]17837 새로운 게임 2
# https://www.acmicpc.net/problem/17837
# https://chldkato.tistory.com/130

dx = [0,0,-1,1]
dy = [1,-1,0,0]
White, Red, Blue = 0,1,2

import sys
input = sys.stdin.readline

def move(num):
  x, y, d = unit[num]
  nx = x + dx[d]
  ny = y + dy[d]

  if nx < 0 or ny < 0 or nx == n or ny == n or arr[nx][ny] == Blue:
    if (d % 2) == 0:
      unit[num][2] = d + 1
    else:
      unit[num][2] = d - 1

    nx = x - dx[d]
    ny = y - dy[d]
  
    if nx < 0 or ny < 0 or nx == n or ny == n or arr[nx][ny] == Blue:
      return False
  
  unitSet = []
  for i, key in enumerate(board[x][y]):
    if key == num:
      unitSet.extend(board[x][y][i:])
      board[x][y] = board[x][y][:i]
      break

  if arr[nx][ny] == Red:
    unitSet = unitSet[::-1]
  
  for i in unitSet:
    board[nx][ny].append(i)
    unit[i][:2] = [nx,ny]
  
  return len(board[nx][ny]) >= 4  

n,m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
board = [[[] for _ in range(n)] for _ in range(n)]

unit = [[] for _ in range(m)]
for i in range(m):
  x,y,d = map(int, sys.stdin.readline().rstrip().split())
  unit[i] = [x-1,y-1,d-1]
  board[x-1][y-1].append(i)

cnt = 1
ans = -1
while cnt <= 1000:
  for i in range(m):
    if move(i):
      ans = cnt
      cnt = 1001
      break
  cnt += 1

print(ans)