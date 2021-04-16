# [S3]1072 게임
# https://www.acmicpc.net/problem/1072
# 시간 복잡도 : O(logn)
# /(나누기)는 float형으로 나와서 조심해야 함

def get_rate(x,y):
  return 100 * y // x
  #return int(y/x*100) - 50 29 -> 27나옴

x, y = map(int, input().split())
z = get_rate(x,y)

if z >= 99:
  print(-1)
else:
  lo = 0
  hi = int(2e9)

  while lo + 1 < hi:
    mid = (lo + hi) // 2
    nx, ny = x + mid, y + mid
    nz = get_rate(nx,ny)
    if z == nz:
      lo = mid
    else:
      hi = mid
  print(hi)