# [S1]2293 동전 1
# https://www.acmicpc.net/problem/2293
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = []
dp = [1] + [0] * k
for _ in range(n):
    arr.append(int(input()))

for x in arr:
    for i in range(1, k+1):
        if i - x >= 0:
            dp[i] += dp[i - x]

print(dp[k])