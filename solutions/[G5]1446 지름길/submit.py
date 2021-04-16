# [G5]1446 지름길
# https://www.acmicpc.net/problem/1446

import sys
from collections import deque
from copy import deepcopy
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x : x[1])
dist = [i for i in range(10001)]

for i in range(1, d+1):
    dist[i] = min(dist[i], dist[i-1] + 1)
    for j in range(len(arr)):
        if i == arr[j][1]:
            dist[i] = min(dist[i], (dist[arr[j][0]] + arr[j][2]))

print(dist[d])