# [G4]2473 세 용액
# https://www.acmicpc.net/problem/2473

# p1고정 후 p2, p3 움직임

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

max = int(3e9) + 1
temp = []
for p1 in range(0, n-1):
    p2, p3 = p1 + 1, n - 1
    while p2 != p3:
        x = arr[p1] + arr[p2] + arr[p3]
        if x == 0:
            print(arr[p1], arr[p2], arr[p3])
            sys.exit()

        if abs(x) < max:
            temp = [arr[p1],arr[p2],arr[p3]]
            max = abs(x)

        if x < 0:
            p2 += 1
        else:
            p3 -= 1

print(*temp)