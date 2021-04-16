# [S1]2343 기타 레슨
# https://www.acmicpc.net/problem/2343
# 시간 복잡도 : O(nlogm) m = (left - right)
# 파라메트릭 서치, 이진탐색
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int,input().split()))
total = sum(arr)

def check(len):
  cnt, temp = 1,0
  for x in arr:
    if temp + x > len:
      cnt += 1
      temp = x
    else:
      temp += x

  return cnt <= m

right = total
left = total//m
answer = right

while left <= right:
  mid = (left + right) // 2
  if mid < max(arr):
    left = mid + 1
    continue

  if check(mid):
    answer = mid
    right = mid - 1
  else:
    left = mid + 1

print(answer)