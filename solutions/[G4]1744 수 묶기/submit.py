# [G4]1744 수 묶기
# https://www.acmicpc.net/problem/1744

import sys
input = sys.stdin.readline

n = int(input())
arr1, arr2 = [], []
answer = 0
for _ in range(n):
    x = int(input())
    if x == 1:
        answer += 1
    else:
        if x <= 0:
            arr1.append(x)
        else:
            arr2.append(x)

arr1.sort()
arr2.sort(reverse=True)
len1, len2 = len(arr1), len(arr2)

for i in range(0,len1,2):
    if i + 1 < len1:
        answer += (arr1[i] * arr1[i+1])
    else:
        answer += arr1[i]

for i in range(0,len2,2):
    if i + 1 < len2:
        answer += (arr2[i] * arr2[i+1])
    else:
        answer += arr2[i]

print(answer)