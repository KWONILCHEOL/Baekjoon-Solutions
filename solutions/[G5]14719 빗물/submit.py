# [G5]14719 빗물
# https://www.acmicpc.net/problem/14719

#벽 만나면 추가

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
temp = list(map(int, input().split()))

for j in range(m):
    for i in range(n-temp[j], n):
        arr[i][j] = 1

total = 0
for i in range(n):
    left = False
    temp = 0
    for j in range(m):
        if left == False:
            left = arr[i][j] == 1
            continue

        if arr[i][j] == 0:
            temp += 1
        elif arr[i][j] == 1:
            total += temp
            temp = 0

print(total)