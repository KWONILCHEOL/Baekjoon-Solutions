# [G5]12865 평범한 배낭
# https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

n, k = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
dp = [0] * (k+1)

for i in range(n):
    w, v = arr[i]
    if w <= k:
        for j in range(k, w - 1, -1):   #for(int j=k; j >= w; j--)
            dp[j] = max(dp[j], dp[j-w] + v)
print(dp[k])