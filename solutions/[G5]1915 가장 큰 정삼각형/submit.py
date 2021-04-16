# [G5]1915 가장 큰 정삼각형
# https://www.acmicpc.net/problem/1915

import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip())))

ans = 0
for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] == 1:
            arr[i][j] = min(arr[i][j-1],arr[i-1][j],arr[i-1][j-1]) + 1
            
for i in range(n):
    ans = max(ans, max(arr[i]))

print(ans**2)