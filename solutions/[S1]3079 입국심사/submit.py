# [S1]3079 입국심사
# https://www.acmicpc.net/problem/3079
# 시간 복잡도 : O(logN)
# 파라메트릭 서치, 이진탐색

import sys
input = sys.stdin.readline

def check(k):
  cnt = 0
  for i in range(n):
    cnt += (k // arr[i])
    if cnt >= m:
      return True
  return False


n,m = map(int,input().split())
arr = []
for _ in range(n):
  arr.append(int(input()))

inf = int(1e18)
lo = int(0)
hi = inf

while (lo + 1 < hi):
  mid = (lo + hi) // 2
  if check(mid) == False: 
    lo = mid
  else: 
    hi = mid

print(hi)