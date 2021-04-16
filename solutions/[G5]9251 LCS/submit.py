# [G5]9251 LCS
# https://www.acmicpc.net/problem/9251

import sys

input = sys.stdin.readline

arr1 = ' ' + input().rstrip()
arr2 = ' ' + input().rstrip()

len1 = len(arr1)
len2 = len(arr2)

dp = [[0] * len2 for _ in range(len1)]

for i in range(1, len1):
    for j in range(1, len2):
        if arr1[i] == arr2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len1 - 1][len2 - 1])