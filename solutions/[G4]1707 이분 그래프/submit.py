# [G4]1707 이분 그래프
# https://www.acmicpc.net/problem/1707

import sys
input = sys.stdin.readline

k = int(input())
for _ in range(k):
    v, e = map(int,input().split())
    arr = [[] for _ in range(v+1)]
    check = [0] * (v+1)
    for _ in range(e):
        a, b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)

    answer = "YES"
    for i in range(1,v+1):
        que = []

        if check[i] == 0:
            que.append(i)
            check[i] = 1

        while que:
            cur = que.pop()
            key = check[cur]
            for x in arr[cur]:
                if  key == check[x]:
                    que.clear()
                    answer = "NO"
                    break
                if check[x] == 0:
                    que.append(x)
                    check[x] = -key

        if answer == "NO":
            break

    print(answer)