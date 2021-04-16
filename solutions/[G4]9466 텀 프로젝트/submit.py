# [G4]9466 텀 프로젝트
# https://www.acmicpc.net/problem/9466

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int,input().split()))
    visit = [0] * (n+1)

    cnt = 0
    time = 0
    for i in range(1,n+1):
        if visit[i] > 0:
            continue
        time += 1
        s, e = i, i

        #순환지점 or 방문했던지점까지
        while visit[e] == 0:
            visit[e] = time
            e = arr[e]

        #방문했던 지점까지 or 시작점부터 순환지점
        while visit[s] == time and s != e:
            cnt += 1
            s = arr[s]

    print(cnt)