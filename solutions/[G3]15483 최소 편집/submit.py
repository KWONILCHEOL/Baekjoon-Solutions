# [G3]15483 최소 편집
# https://www.acmicpc.net/problem/15483
# [G2]7620 편집 거리
# https://www.acmicpc.net/problem/7620
# 참고 : https://hsp1116.tistory.com/41

import sys
input = sys.stdin.readline

arr1 = ' ' + input().rstrip()
arr2 = ' ' + input().rstrip()

len1 = len(arr1)
len2 = len(arr2)

dp = [[0] * len2 for _ in range(len1)]
for i in range(len1):
  dp[i][0] = i
  
for j in range(len2):
  dp[0][j] = j

for i in range(1, len1):
  for j in range(1, len2):
    if arr1[i] == arr2[j]:
      dp[i][j] = dp[i-1][j-1]
    else:
      dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

# for i in range(len1):
#   for j in range(len2):
#     print(dp[i][j], end = ' ')
#   print()

print(dp[len1-1][len2-1])