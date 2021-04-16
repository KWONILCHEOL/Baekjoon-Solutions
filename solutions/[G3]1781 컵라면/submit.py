# [G3]1781 컵라면
# https://www.acmicpc.net/problem/1781

import sys
import heapq
input = sys.stdin.readline

n = int(input())
hq = []
length = 0
for x in sorted([list(map(int,input().split())) for _ in range(n)],key=lambda x : x[0]):
    if length < x[0]:  #len(hq) 현재 시간, x[0] 데드라인
        heapq.heappush(hq, x[1])
        length += 1
    elif hq[0] < x[1]:  #데드라인이 현재 시간보다 작고, 제일 작은 컵라면수와 비교
        heapq.heappop(hq)
        heapq.heappush(hq, x[1])

print(sum(hq))