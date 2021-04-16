# [G5]1759 암호 만들기
# https://www.acmicpc.net/problem/1759

import sys
from itertools import combinations
input = sys.stdin.readline

vowels = ['a','e','i','o','u']

l, c = map(int, input().split())
alpha = sorted(list(input().rstrip().split()))
answer = []
for x in combinations(alpha, l):
    x = ''.join(x)
    vowels_n = 0
    consonants_n = 0
    for c in x:
        if c in vowels:
            vowels_n += 1
        else:
            consonants_n += 1
        if vowels_n >= 1 and consonants_n >= 2:
            answer.append(x)
            break

for x in answer:
    print(x)