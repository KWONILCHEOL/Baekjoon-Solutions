# [S1]18222 투에-모스 문자열
# https://www.acmicpc.net/problem/18222

import sys
from math import log2
from math import pow
input = sys.stdin.readline

def number(x):
    if x == 1:
        return 1
    n = int(log2(x))
    x = x - int(pow(2, n))
    if x == 0:
        x = int(pow(2,n)) // 2
    return 1 + number(x)

k = int(input())
cnt = number(k)
print(0 if cnt % 2 else 1)