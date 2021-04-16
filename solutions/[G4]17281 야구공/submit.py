# [G4]17281 야구공
# https://www.acmicpc.net/problem/17281

import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
max_score = 0

permu = [1,2,3,4,5,6,7,8]
for player in permutations(permu, 8):
    player = list(player)
    player = player[:3] + [0] + player[3:]
    score = 0
    i = 0
    for inning in range(1, n+1):
        out = 0
        base1, base2, base3 = 0,0,0
        while out < 3:
            if arr[inning-1][player[i]] == 0:
                out += 1
            elif arr[inning-1][player[i]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif arr[inning-1][player[i]] == 2:
                score += (base2 + base3)
                base1, base2, base3 = 0,1,base1
            elif arr[inning-1][player[i]] == 3:
                score += (base1 + base2 + base3)
                base1, base2, base3 = 0,0,1
            elif arr[inning-1][player[i]] == 4:
                score += (base1 + base2 + base3 + 1)
                base1, base2, base3 = 0,0,0
            i += 1
            i %= 9
    max_score = max(max_score, score)
print(max_score)