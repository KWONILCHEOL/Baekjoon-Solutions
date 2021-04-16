# [G2]2266 금고 테스트
# https://www.acmicpc.net/problem/2266

import sys
input = sys.stdin.readline
INF = int(1e9)

n,k = map(int,input().split())
dp = [[0] * (n+1) for _ in range(k+1)]
for i in range(1, k+1):
    dp[i][1] = 1

for i in range(1, n+1):
    dp[1][i] = i

for i in range(2, k+1):
    for j in range(2, n+1):
        dp[i][j] = INF
        for f in range(1, j+1):
            res = 1 + max(dp[i-1][f-1], dp[i][j-f])
            dp[i][j] = min(dp[i][j], res)

print(dp)
print(dp[k][n])
