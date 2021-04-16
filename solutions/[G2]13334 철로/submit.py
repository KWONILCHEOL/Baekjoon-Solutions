# [G2]13334 철로
# https://www.acmicpc.net/problem/13334

# 철로는 오른쪽 기준(b-d)
# 철로보다 왼쪽에 있으면 제거
import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
d = int(input())

# [전처리] 시간초과 원인
# for a, b in arr[:]:
#     if abs(a - b) > d:
#         arr.remove([a,b])

for i in range(len(arr)):
    if arr[i][0] > arr[i][1]:
        arr[i] = [arr[i][1], arr[i][0]]
arr.sort(key=lambda x : (x[1]))

answer = 0
hq = []
for a,b in arr:
    x = b - d
    heapq.heappush(hq, [a,b])
    while len(hq) > 0 and hq[0][0] < x:
        heapq.heappop(hq)
    answer = max(answer, len(hq))

print(answer)