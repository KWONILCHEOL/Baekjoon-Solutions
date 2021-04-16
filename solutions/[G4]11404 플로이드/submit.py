# [G4]11404 플로이드
# https://www.acmicpc.net/problem/11404

import sys
input = sys.stdin.readline
n = int(input())
testCase = int(input())
for _ in range(testCase):
  n,m = map(int, input().split())
  arr = list(map(int,input().split()))

  dp = []
  for i in range(n):
    dp.append(arr[i * m : i * m + m])
  
  for j in range(1, m):
    for i in range(n):
      left = dp[i][j-1]
      left_up = dp[i-1][j-1] if i > 0 else 0
      left_down = dp[i+1][j-1] if i < (n - 1) else 0
      
      dp[i][j] += max(left, left_up, left_down)
      
  #for j in range(1, m):
  #   for i in range(n):
  #     dp[i][j] = 0 + max(dp[i][j],(dp[i][j-1]+arr[i*m + j]))
  #     if i > 0:
  #       dp[i][j] = 0 + max(dp[i][j],(dp[i-1][j-1]+arr[i*m + j]))
  #     if i < n - 1:
  #       dp[i][j] = 0 + max(dp[i][j],(dp[i+1][j-1]+arr[i*m + j]))
  
  result = 0
  for i in range(n):
    result = max(result, dp[i][m-1])

  print(result)