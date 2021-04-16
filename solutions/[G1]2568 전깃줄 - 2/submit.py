# [G1]2568 전깃줄 - 2
# https://www.acmicpc.net/problem/2568
# [S1]2565 전깃줄
# https://www.acmicpc.net/problem/2565

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()
dp = []
connect = [[0]]
for i,x in enumerate(arr):
    idx = bisect_left(dp, x[1])
    
    # if idx < len(dp) == True이면
    # 이전 dp[idx]는 dp[idx-1]과 연관있음
    if idx < len(dp):
        dp[idx] = x[1]
        connect[idx + 1] = connect[idx] + [x[0]]
    else:
        dp.append(x[1])
        connect.append(connect[-1] + [x[0]])
    arr[i] = x[0]

ans = set(arr).difference(set(connect[-1]))

print(len(ans))
for x in ans:
    print(x)