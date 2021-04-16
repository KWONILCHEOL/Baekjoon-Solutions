# [G5]9663 N-Queen
# https://www.acmicpc.net/problem/9663

import sys
input = sys.stdin.readline

def go(x):
    if x == n:
        return 1

    cnt = 0
    for y in range(n):
        if col[y] and diagonal_left[x+y] and diagonal_right[x-y+n-1]:
            col[y] = False
            diagonal_left[x+y] = False
            diagonal_right[x-y+n-1] = False
            cnt += go(x+1)
            col[y] = True
            diagonal_left[x+y] = True
            diagonal_right[x-y+n-1] = True

    return cnt

n = int(input())
col = [True] * n
diagonal_left = [True] * (2 * n - 1)
diagonal_right = [True] * (2 * n - 1)
print(go(0))