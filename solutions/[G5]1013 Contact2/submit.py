# [G5]1013 Contact
# https://www.acmicpc.net/problem/1013

import sys,re
input = sys.stdin.readline
n = int(input())

pattern=re.compile("(100+1+|01)+")

for _ in range(n):
    s = input().strip()
    if re.fullmatch(pattern,s):
        print("YES")
    else:
        print("NO")