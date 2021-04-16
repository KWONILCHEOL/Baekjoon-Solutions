# [G4]8980 택배
# https://www.acmicpc.net/problem/8980

import sys
input = sys.stdin.readline

n, c = map(int,input().split())
m = int(input())
arr = [list(map(int,input().split())) for _ in range(m)]
arr.sort(key=lambda x:(x[0],x[1]))
truck = [0] * (n+1)

i = 0
pos = 0
nowBox = 0
result = 0

for i in range(n+1):
    if pos == m:
        break

    if truck[i] > 0:
        nowBox -= truck[i]
        result += truck[i]
        truck[i] = 0

    while pos < m:
        a, b, box = arr[pos]
        if i < a:
            break
        pos += 1

        if nowBox + box <= c:
            nowBox += box
            truck[b] += box
        elif nowBox + box > c:  #초과 시
            #가능한 만큼 채우기
            box -= (c - nowBox)
            truck[b] += (c - nowBox)
            nowBox += (c - nowBox)

            # 뒤쪽을 비우고 앞쪽 채우기
            for j in range(n, b, -1):
                if truck[j] > 0:
                    if box >= truck[j]:
                        truck[b] += truck[j]
                        truck[j] = 0
                    elif box < truck[j]:
                        truck[b] += box
                        truck[j] -= box
                        break
result += nowBox
print(result, end='')