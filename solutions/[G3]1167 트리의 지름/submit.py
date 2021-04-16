# [G3]1167 트리의 지름
# https://www.acmicpc.net/problem/1167

import sys
input = sys.stdin.readline

def dfs(cur):
    global answer
    temp = [0]
    check[cur] = True
    for node, dist in T[cur]:
        if check[node]:
            continue
        temp.append(dfs(node) + dist)

    if len(temp) >= 2:
        temp.sort()
        answer = max(temp[-1] + temp[-2], answer)
    return temp[-1]


n = int(input())
T = [[] for _ in range(n + 1)]
check = [False] * (n + 1)
for i in range(1, n+1):
    temp = list(map(int,input().split()))
    length = len(temp)
    for j in range(1, length - 1, 2):
        T[temp[0]].append((temp[j], temp[j+1]))

answer = 0
dfs(1)
print(answer)