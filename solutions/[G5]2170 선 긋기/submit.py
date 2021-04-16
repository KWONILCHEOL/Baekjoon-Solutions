# [G5]2170 선 긋기
# https://www.acmicpc.net/problem/2170

#하나라도 중간값이게 되면 구간 재설정

import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([tuple(map(int, input().split())) for _ in range(n)])

lines = []
for i in range(n):
    a2, b2 = arr[i]
    flag = False
    for j in range(len(lines)):
        a1, b1 = lines[j]
        if a1 <= a2 <= b1 and a1 <= b2 <= b1:
            flag = True
            break
        if a1 <= a2 <= b1:
            lines[j] = (a1, b2)
            flag = True
            break
        elif a1 <= b2 <= b1:
            lines[j] = (a2, b1)
            flag = True
            break

    if flag == False:
        lines.append((a2, b2))

total = 0
for a, b in lines:
    total += b - a

print(total)