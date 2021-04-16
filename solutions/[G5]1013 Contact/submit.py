# [G5]1013 Contact
# https://www.acmicpc.net/problem/1013
#1(0)2, 1(1)3
#2(0)x, 2(1)1
#3(0)4, 3(1)x
#4(0)5, 4(1)x
#5(0)5, 5(1)6
#6(0)2, 6(1)7
#7(0)8, 7(1)7
#8(0)5, 8(1)1
#final 1,6,7

import sys
input = sys.stdin.readline

arr = [[],[2,3],[-1,1],[4,-1],[5,-1],[5,6],[2,7],[8,7],[5,1]]
def check():
    state = 1
    for x in pattern:
        x = int(x)
        state = arr[state][x]
        if state == -1:
            return "NO"

    if state == 1 or state == 6 or state == 7:
        return "YES"

    return "NO"
n = int(input())
for _ in range(n):
    pattern = input().rstrip()
    print(check())