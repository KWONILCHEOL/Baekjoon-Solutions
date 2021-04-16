# [G3]16947 서울 지하철 2호선
# https://www.acmicpc.net/problem/16947

import sys
input = sys.stdin.readline

n = int(input())
visit = [False] * (n+1)
G = [[] for _ in range(n+1)]
GSize = [0] * (n+1)
parent = [0] * (n+1)
ans = [0] * (n+1)
for _ in range(n):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    GSize[a] += 1
    GSize[b] += 1

while 1 in GSize:
    for i in range(1, n+1):
        if GSize[i] != 1:       #리프노드의 부모 구하기
            continue
        parent[i] = G[i][0]
        GSize[i] = 0            #리프노드 제거
        GSize[parent[i]] -= 1
        G[parent[i]].remove(i)  #역방향 제거

while any(parent):
    for i in range(1, n+1):
        if parent[i] == 0:
            continue
        if parent[parent[i]] == 0:
            ans[i] = ans[parent[i]] + 1
            parent[i] = 0

print(*ans[1:])