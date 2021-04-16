# [G3]16434 드래곤 앤 던전
# https://www.acmicpc.net/problem/16434

# 괴물 만났을때 감소되는 체력 = 괴물공격력 * ((괴물 체력 - 1) // 내 공격력))

import sys
input = sys.stdin.readline
INF = int(1e19)
hp = 0
n, atk = map(int,input().split())
min_hp, max_hp = INF, 0
temp = []
for _ in range(n):
    temp.append(list(map(int, input().split())))

for i in range(n):
    t, a, h = temp[i]
    #atk, hp +- 나누기 귀찮아서 한번에 해결
    if t == 1:
        temp[i][2] = - (a * ((h-1)//atk))
        temp[i][1] = 0

    atk += temp[i][1]
    hp += temp[i][2]

    max_hp = max(max_hp, hp)
    min_hp = min(min_hp, hp - max_hp)

print(-min_hp + 1)