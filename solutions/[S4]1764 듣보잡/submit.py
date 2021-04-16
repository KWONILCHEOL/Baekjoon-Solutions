# [S4]1764 듣보잡
# https://www.acmicpc.net/problem/1764
# 중복되는 문자열 
# set &연산 이용

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set()
b = set()
for _ in range(n):
    a.add(input().rstrip())
    
for _ in range(m):
    b.add(input().rstrip())

ret = list(a&b)
ret.sort()
print(len(ret))
for x in ret:
    print(x)