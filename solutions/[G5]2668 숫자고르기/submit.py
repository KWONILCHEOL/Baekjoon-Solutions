# [G5]2668 숫자고르기
# https://www.acmicpc.net/problem/2668

#순환 + 자신
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
visited = [-1] * (n+1)
answer = []

for i in range(1,n+1):
    if i == arr[i]:
        visited[i] = 0;
        answer.append(i)

cnt = 0
for i in range(1, n+1):
    if visited[i] == -1:
        cnt += 1
        x = i
        start = -1
        while True:
            if visited[x] == -1:
                visited[x] = cnt
                x = arr[x]
                continue

            if visited[x] == cnt:
                start = x

            break

        if start > 0:
            answer.append(start)
            x = arr[start]
            while x != start:
                answer.append(x)
                x = arr[x]

print(len(answer))
for x in sorted(answer):
    print(x)