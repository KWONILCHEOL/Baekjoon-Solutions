# [G3]16986 인싸들의 가위바위보
# https://www.acmicpc.net/problem/16986

import sys
from itertools import permutations
input = sys.stdin.readline

n, k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
hee = list(map(int, input().split()))
ho = list(map(int, input().split()))

for woo in permutations(list(range(n)), n):
    woo_score = 0
    hee_score = 0
    ho_score = 0
    woo = list(woo)
    for i in range(1, n, 2):
        woo_hee = arr[woo[i-1]][hee[i-1] - 1]
        if woo_hee == 2:
            woo_score += 1
        else:
            hee_score += 1

        if hee_score == k:
            break
        elif ho_score == k:
            break
        elif woo_score == k:
            print("1")
            sys.exit()

        hee_ho = arr[hee[i] - 1][ho[i-1] - 1]
        if hee_ho == 2:
            hee_score += 1
        else:
            ho_score += 1

        if hee_score == k:
            break
        elif ho_score == k:
            break
        elif woo_score == k:
            print("1")
            sys.exit()

        ho_woo = arr[woo[i]][ho[i] - 1]
        if ho_woo == 0:
            woo_score += 1
        else:
            ho_score += 1

        if hee_score == k:
            break
        elif ho_score == k:
            break
        elif woo_score == k:
            print("1")
            sys.exit()

print("0")

