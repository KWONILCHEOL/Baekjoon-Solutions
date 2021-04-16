# [G5]2225 합분해
# https://www.acmicpc.net/problem/2225

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
d = [[0] * (n+1) for _ in range(k+1)]
d[0][0] = 1
for i in range(1, k + 1):
    for j in range(n + 1):
        for x in range(j + 1):
            d[i][j] = (d[i][j] + d[i-1][j-x]) % int(1e9)

# for i in range(1, k+1):
#     print(d[i])

print(d[k][n])