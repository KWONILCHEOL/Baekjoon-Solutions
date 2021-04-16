# [G4]2136 개미
# https://www.acmicpc.net/problem/2136

import sys
input = sys.stdin.readline

stick = []
plus = 0
minus = 0
maxMove = 0

n, l = map(int,input().split())
for i in range(1, n+1):
    x = int(input())
    if x >= 0:
        stick.append((x,i))
        plus += 1
        x = l - x
    else:
        stick.append((-x,i))
        minus += 1

    if abs(maxMove) < abs(x):
        maxMove = x
stick.sort(key=lambda x : x[0])

# (minus-1) 또는 (minus)번째 개미가 마지막에 떨어짐
# minus-1은 왼쪽, minus는 오른쪽으로 떨어짐

if maxMove > 0:
    print(stick[minus][1], maxMove, end='')
else:
    print(stick[minus - 1][1], -maxMove, end='')