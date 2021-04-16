# [G5]2631 줄세우기
# https://www.acmicpc.net/problem/2631

import sys
input = sys.stdin.readline

n = int(input())
A = [int(input()) for _ in range(n)]
dp = [1] * (n)

for i in range(n):
    for j in range(i+1):
        if A[i] > A[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(n - max(dp))