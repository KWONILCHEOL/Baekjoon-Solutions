# [G3]2352 반도체 설계
# https://www.acmicpc.net/problem/2352
# 시간 복잡도 : O(nlogn)

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = [[]for _ in range(n + 1)]

answer = 1
dp[1] = arr[0]

for i in range(1, n):
  if(dp[answer] < arr[i]):
    answer += 1
    dp[answer] = arr[i]
  else:
    index = bisect_left(dp[1:answer+1], arr[i])
    dp[index + 1] = arr[i]

print(answer)