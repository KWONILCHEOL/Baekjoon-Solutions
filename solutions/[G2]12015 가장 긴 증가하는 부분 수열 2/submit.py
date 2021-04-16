# [G2]12015 가장 긴 증가하는 부분 수열 2
# https://www.acmicpc.net/problem/12015
# 시간 복잡도 : O(nlogn)

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = []

for x in arr:
  index = bisect_left(dp, x)
  if index < len(dp):
    dp[index] = x
  else:
    dp.append(x)

print(len(dp))