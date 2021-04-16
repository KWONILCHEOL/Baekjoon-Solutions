# [G5]15686 치킨 배달
# https://www.acmicpc.net/problem/15686

#집은 h에, 가게는 s에 정리한 후 백트레킹
#itertools.permutation를 사용하면 시간초과
#dfs는 combinations를 사용함

import sys
input = sys.stdin.readline

def go(idx, n):
    global result, m, house, store, c
    if n == m:
        _sum = 0
        for hx,hy in house:
            _min = 100
            for j in range(m):
                _min = min(_min, abs(hx-store[c[j]][0]) + abs(hy-store[c[j]][1]))
            _sum += _min
        result = min(result, _sum)
        return

    if idx == store_n:
        return

    c[n] = idx
    go(idx + 1, n + 1)
    c[n] = 0
    go(idx + 1, n)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

n, m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
c = [0] * m
house = []
store = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i,j))
        elif arr[i][j] == 2:
            store.append((i,j))

store_n = len(store)

result = 10000
go(0, 0)

print(result)