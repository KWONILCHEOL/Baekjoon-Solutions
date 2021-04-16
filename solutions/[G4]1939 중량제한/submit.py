# [G4]1939 중량제한
# https://www.acmicpc.net/problem/1939
# 시간 복잡도 : O(nlogc)

def check(cost):    #O(n)
  que = []
  que.append(s)
  visit = [False for _ in range(n + 1)]
  visit[s] = True

  while que:
    x = que.pop()
    
    for b,c in arr[x]:
      if visit[b] == False and cost <= c:
        if b == e:
          return True
        visit[b] = True
        que.append(b)
  
  return False

import sys
n,m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]

lo, hi = 1,1
answer = 1
for _ in range(m):
  a, b, c = map(int, sys.stdin.readline().split())
  arr[a].append([b,c])
  arr[b].append([a,c])
  hi = max(hi,c)

s, e = map(int, sys.stdin.readline().split())

while lo <= hi:     #O(logc)
  mid = (lo + hi) // 2
  if check(mid):
    lo = mid + 1
  else:
    hi = mid - 1

print(hi)