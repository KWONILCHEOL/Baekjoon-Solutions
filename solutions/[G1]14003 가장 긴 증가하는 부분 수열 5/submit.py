# [G1]14003 가장 긴 증가하는 부분 수열 5
# https://www.acmicpc.net/problem/14003
# [G4]14002 가장 긴 증가하는 부분 수열 4
# https://www.acmicpc.net/problem/14002

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = []
connect = [[0]]
for x in arr:
    index = bisect_left(dp, x)
    if index < len(dp):
        dp[index] = x
        connect[index + 1] = connect[index] + [x]
    else:
        dp.append(x)
        connect.append(connect[-1] + [x])

answer = connect[-1][1:]
print(len(answer))
print(*answer)