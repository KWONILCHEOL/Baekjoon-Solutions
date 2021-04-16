# [S1]2294 동전 2
# https://www.acmicpc.net/problem/2294

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = []
dp = [0] + [10001] * k
for i in range(n):
    arr.append(int(input()))
    if arr[i] <= k:
        dp[arr[i]] = 1

for i in range(1, k+1):
    for x in arr:
        if i - x >= 0:
            dp[i] = min(dp[i], dp[i-x]+1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])