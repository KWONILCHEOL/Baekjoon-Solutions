# [G5]14500 테트로미노
# https://www.acmicpc.net/problem/14500

import sys
input = sys.stdin.readline
n, m = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if j + 3 < m:
            ans = max(ans, A[i][j] + A[i][j + 1] + A[i][j + 2] + A[i][j + 3])
        if i + 3 < n:
            ans = max(ans, A[i][j] + A[i + 1][j] + A[i + 2][j] + A[i + 3][j])

        if i + 1 < n and j + 1 < m:
            ans = max(ans, A[i][j] + A[i][j + 1] + A[i + 1][j] + A[i + 1][j + 1])

        if i + 2 < n and j + 1 < m:
            ans = max(ans, A[i][j] + A[i + 1][j] + A[i + 2][j] + A[i + 2][j + 1])
            ans = max(ans, A[i][j + 1] + A[i + 1][j + 1] + A[i + 2][j + 1] + A[i + 2][j])
            ans = max(ans, A[i][j] + A[i][j + 1] + A[i + 1][j] + A[i + 2][j])
            ans = max(ans, A[i][j] + A[i][j + 1] + A[i + 1][j + 1] + A[i + 2][j + 1])

            ans = max(ans, A[i][j] + A[i + 1][j] + A[i + 1][j + 1] + A[i + 2][j + 1])
            ans = max(ans, A[i][j + 1] + A[i + 1][j] + A[i + 1][j + 1] + A[i + 2][j])

            ans = max(ans, A[i][j] + A[i + 1][j] + A[i + 1][j + 1] + A[i + 2][j])
            ans = max(ans, A[i][j + 1] + A[i + 1][j] + A[i + 1][j + 1] + A[i + 2][j + 1])

        if i + 1 < n and j + 2 < m:
            ans = max(ans, A[i][j] + A[i][j + 1] + A[i][j + 2] + A[i + 1][j])
            ans = max(ans, A[i][j] + A[i][j + 1] + A[i][j + 2] + A[i + 1][j + 2])
            ans = max(ans, A[i][j] + A[i + 1][j] + A[i + 1][j + 1] + A[i + 1][j + 2])
            ans = max(ans, A[i][j + 2] + A[i + 1][j] + A[i + 1][j + 1] + A[i + 1][j + 2])

            ans = max(ans, A[i][j] + A[i][j + 1] + A[i + 1][j + 1] + A[i + 1][j + 2])
            ans = max(ans, A[i][j + 1] + A[i][j + 2] + A[i + 1][j] + A[i + 1][j + 1])

            ans = max(ans, A[i][j] + A[i][j + 1] + A[i][j + 2] + A[i + 1][j + 1])
            ans = max(ans, A[i][j + 1] + A[i + 1][j] + A[i + 1][j + 1] + A[i + 1][j + 2])

print(ans)