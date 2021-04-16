# [G2]9370 미확인 도착지
# https://www.acmicpc.net/problem/9370

import sys
import heapq
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(s):
    distance = [INF] * (n+1)
    distance[s] = 0
    q = []
    heapq.heappush(q, (0,s))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for x in graph[now]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))

    return distance




t = int(input())
for _ in range(t):
    n,m,t = map(int,input().split())
    s,h,g = map(int,input().split())

    graph = [[]  for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))

    dest = []
    for _ in range(t):
        dest.append(int(input()))
    dest.sort()

    distanceS = dijkstra(s)
    if distanceS[h] < distanceS[g]:
        h = g

    distanceH = dijkstra(h)
    ans = []
    for x in dest:
        total = distanceS[h] + distanceH[x]
        if distanceS[x] == total:
            ans.append(x)

    print(*ans)


# 2
# 5 4 2
# 1 2 3
# 1 2 6
# 2 3 2
# 3 4 4
# 3 5 3
# 5
# 4
# 6 9 2
# 2 3 1
# 1 2 1
# 1 3 3
# 2 4 4
# 2 5 5
# 3 4 3
# 3 6 2
# 4 5 4
# 4 6 3
# 5 6 7
# 5
# 6