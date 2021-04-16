# [G3]1300 K번째 수
# https://www.acmicpc.net/problem/1300

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

left = 1
right = k
result = 0

while left <= right:
    mid = (left + right) >> 1
    num = 0
    for i in range(1, n+1):
        num += min(mid//i, n)   #i행 또는 i열에서 mid보다 작은게 몇개인가?
    if num < k:
        left = mid + 1
    else:
        result = mid
        right = mid - 1

print(result)