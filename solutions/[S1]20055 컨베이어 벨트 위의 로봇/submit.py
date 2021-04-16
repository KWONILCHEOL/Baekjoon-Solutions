# [S1]20055 컨베이어 벨트 위의 로봇
# https://www.acmicpc.net/problem/20055

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
check = [False] * (2 * n)
q = deque()
s = 0
ans = 1
while m > 0:
    #1. 벨트가 한 칸 회전한다.
    s = (s - 1 + 2 * n) % (2 * n)

    #2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    #   만약 이동할 수 없다면 움직이지 않는다.
    length = len(q)
    for i in range(length):
        x = q.pop()

        #회전 시 로봇이 떨어지는 경우
        if x == ((s + n - 1) % (2 * n)):
            check[x] = False
            continue

        nx = ((x + 1) % (2 * n))
        #이동 가능
        if arr[nx] > 0 and check[nx] == False:
            check[x] = False
            arr[nx] -= 1

            if nx != ((s + n - 1) % (2 * n)):
                check[nx] = True
                q.append(nx)

            if arr[nx] == 0:
                m -= 1

        #이동 불가
        elif x != ((s + n - 1) % (2 * n)):
            q.append(x)

    #3. 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if arr[s] > 0:
        arr[s] -= 1
        check[s] = True
        q.append(s)
        if arr[s] == 0:
            m -= 1
    #4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if m <= 0:
        break

    ans += 1
print(ans)