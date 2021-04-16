# [S3]19941 햄버거 분배
# https://www.acmicpc.net/problem/19941

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
table = input()
H = deque()
P = deque()
for i in range(n):
    if table[i] == 'H':
        H.append(i)
    else:
        P.append(i)

answer = 0
while P:
    p = P.popleft()
    while H:
        h = H.popleft()
        if abs(h - p) <= k:
            answer+=1
            break
        if h - p > k:
            H.appendleft(h)
            break
print(answer)