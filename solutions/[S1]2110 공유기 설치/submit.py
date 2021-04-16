# [S1]2110 공유기 설치
# https://www.acmicpc.net/problem/2110
# 파라메트릭 서치, 이진탐색

def check(k):
  value = arr[0]
  cnt = 1
  for i in range(1,n):
    if arr[i] >= value + k:
      value = arr[i]
      cnt += 1
      if cnt == c:
        return True
  return False

import sys
input = sys.stdin.readline

n,c = list(map(int, input().split()))
arr = []
for _ in range(n):
  arr.append(int(input()))
arr.sort()

lo = 1 #최소 gap
hi = arr[-1] - arr[0]  #최대 gap
result = 0

while lo + 1 < hi: #O(logN)
  mid = (lo + hi) // 2
  if check(mid) == False:
    hi = mid
  else:
    lo = mid
    result = mid

  value = arr[0]
  cnt = 1

print(lo)