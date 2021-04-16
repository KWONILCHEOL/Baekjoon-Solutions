# [G5]5014 스타트링크
# https://www.acmicpc.net/problem/5014
# 시간복잡도 : O(2^n)

import sys
input = sys.stdin.readline

f,s,g,u,d = map(int, input().rstrip().split())

#시작지점과 도착지점이 같음
if s == g:
  print(0)
  sys.exit()

que = [s]

#방문 확인
visit = [False] * (f + 1)
visit[s] = True
cnt = 0

while(len(que) > 0):
  length = len(que)
  #시도 횟수
  cnt += 1
  #반복문으로 bfs(위, 아래) 구현
  for _ in range(length):
    x = que[0]
    que.pop(0)

    nu = x + u
    nd = x - d
    if nu == g or nd == g:
      print(cnt)
      sys.exit()
    
    if nu <= f and visit[nu] == False:
      que.append(nu)
      visit[nu] = True
    
    if nd >= 1 and visit[nd] == False:
      que.append(nd)
      visit[nd] = True

print("use the stairs")