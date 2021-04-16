# [G3]20129 뒤집힌 계산기
# https://www.acmicpc.net/problem/20129

# 나누기 -> int(a/b)

import re
import sys
from collections import deque

input = sys.stdin.readline

arr = list(map(int,input().split()))
x1 = input().rstrip()

p = re.compile("[0-9]+")
x2 = deque(map(int, p.findall(x1)))
x2.reverse()

p = re.compile("[^0-9]")
x3 = deque(p.findall(x1))
x3.reverse()

p = ['.'] * 4
p[arr[0] - 1] = '+'
p[arr[1] - 1] = '-'
p[arr[2] - 1] = '*'
p[arr[3] - 1] = '/'
p.reverse()

b = x2.popleft()
for op in p:
    for _ in range(len(x3)):
        a = b
        b = x2.popleft()
        o = x3.popleft()

        if op == o:
            if op == '+':
                b = a + b
            elif op == '-':
                b = a - b
            elif op == '*':
                b = a * b
            elif op == '/':
                b = int(a/b)
        else:
            x2.append(a)
            x3.append(o)
    x2.append(b)
    b = x2.popleft()
print(b)