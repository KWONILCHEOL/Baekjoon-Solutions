# [G4]8983 사냥꾼
# https://www.acmicpc.net/problem/8983

import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
m = sorted(list(map(int, input().split())))
animal = [list(map(int, input().split())) for _ in range(N)]
animal = list(filter(lambda x: x[1] <= L, animal))
ans = 0
for a, b in animal:
    # 동물 기준으로 사냥 가능한 left, right
    left = a + b - L
    right = a - b + L

    low, high = 0, M - 1
    while low <= high:
        mid = (low + high) // 2
        if left <= m[mid] <= right:
            ans += 1
            break

        if m[mid] < left:
            low = mid + 1
        else:
            high = mid - 1

print(ans)