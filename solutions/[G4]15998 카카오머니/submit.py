# [G4]15998 카카오머니
# https://www.acmicpc.net/problem/15998

import sys
from math import gcd
input = sys.stdin.readline
INF = int(1e19)

n = int(input())
M = set()
a,b,c,d = 0,0,0,0
min_M = 0
for _ in range(n):
    c, d = map(int,input().split())
    if b + c > 0 and b + c != d:
        print(-1)
        sys.exit()
    if b + c < 0:
        M.add(d-c-b)
        min_M = max(min_M, d)
    a, b = c, d

min_M += 1
M = list(M)

if len(M) > 0:
    gcd_M = gcd(M[0],M[0])
    for x in M[1:]:
        gcd_M =gcd(gcd_M, x)
        if gcd_M < min_M:
            break

    print(gcd_M if min_M <= gcd_M else -1)
else:
    print(1)