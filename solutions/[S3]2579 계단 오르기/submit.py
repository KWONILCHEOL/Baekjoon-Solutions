# [S3]2579 계단 오르기
# https://www.acmicpc.net/problem/2579

import sys
input = sys.stdin.readline

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

if len(arr) == 2:
    print(arr[1])
    sys.exit()

dp = [0] * (n + 1)
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]
for i in range(3, n + 1):
    #1칸 전 또는 2칸 전을 건너뛸 경우 최대
    dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i] + arr[i-1])
print(dp[n])