# [G5]15681 트리와 쿼리
# https://www.acmicpc.net/problem/15681
# 시간복잡도 : O(n^2)

import sys
#재귀 최대 깊이 설정
sys.setrecursionlimit(123456)
input = sys.stdin.readline

def DFS(cur):
  if c[cur] != 0:
    return c[cur]

  c[cur] = 1
  for next in t[cur]:
    if not c[next]:
      c[cur] += DFS(next)

  return c[cur]

n,r,q = map(int, input().split())
t = [[] for i in range(n+1)]
c = [0] * (n+1)

for _ in range(n-1):
  a, b = map(int, input().split())
  t[a].append(b)
  t[b].append(a)

DFS(r)
for _ in range(q):
  print(c[int(input())])