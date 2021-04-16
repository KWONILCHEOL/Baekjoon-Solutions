# [S4]14501 퇴사
# https://www.acmicpc.net/problem/14501
# 다이나믹 프로그래밍, 브루트포스

import sys
input = sys.stdin.readline

n = int(input())
arr = [0]
dp = [0] + [0] * n
for _ in range(n):
  arr.append(list(map(int, input().split())))

for i in range(1,n+1):
  dp[i] = max(dp[i], dp[i-1])
 
  x = i + arr[i][0] - 1
  if x <= n:
    dp[x] = max(dp[x], dp[i-1] + arr[i][1])

print(max(dp))