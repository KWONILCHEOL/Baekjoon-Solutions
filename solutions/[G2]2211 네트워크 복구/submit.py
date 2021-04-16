# [G2]2211 네트워크 복구
# https://www.acmicpc.net/problem/2211

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(s):
    d = [INF] * (n+1)
    p = [None] * (n+1)
    d[s] = 0

    q = []
    heapq.heappush(q, (0,s))

    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue

        for x in graph[now]:
            cost = dist + x[1]
            if cost < d[x[0]]:
                d[x[0]] = cost
                p[x[0]] = now
                heapq.heappush(q, (cost, x[0]))

    return p

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

parent = dijkstra(1)

print(n-1)
for i in range(2, n+1):
    print(i, parent[i])

# 4 5
# 1 2 1
# 1 4 4
# 1 3 2
# 4 2 2
# 4 3 3