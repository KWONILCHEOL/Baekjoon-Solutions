# [G4]17142 연구소 3
# https://www.acmicpc.net/problem/17142

"""
    빈칸 구간 나누기 - get_empty_section()
    바이러스가 커버가능한 구간 찾기 - get_virus_section()
    초기 바이러스가 끝까지 퍼질 수 있는지 확인 - 빈간 구간 수 와 전체 바이러스 구간 비교
    바이러스들 조합 - list(combinations(virus, m))

"""

import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

dx, dy = [0,1,0,-1], [1,0,-1,0]

#빈칸 구간 나누기
def get_empty_section():
    visit = [[False] * n for _ in range(n)]

    section = [[0] * n for _ in range(n)]
    sec = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == True or arr[i][j] != 0:
                continue

            sec += 1
            q = deque([[i, j]])
            visit[i][j] = True
            section[i][j] = sec
            while len(q) > 0:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx == n or ny == n:
                        continue
                    if visit[nx][ny] == True or arr[nx][ny] == 1:
                        continue

                    q.append([nx, ny])
                    section[nx][ny] = sec
                    visit[nx][ny] = True

    return section, sec

#바이러스 리스트
def get_virus():
    ret = deque([])
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                ret.append([i,j])

    return ret

#바이러스가 커버가능한 구간 찾기
def get_virus_section(virus):
    section = set()
    visit = [[False] * n for _ in range(n)]
    for x,y in virus:
        visit[x][y] = True
        if empty_section[x][y] > 0:
            section.add(empty_section[x][y])

    return len(section)

def solution():
    iRet = 2500
    for temp in list(combinations(virus, m)):
        q = deque(list(temp))
        #현재 조합으로 가능한지 확인
        virus_section_n = get_virus_section(q)
        if empty_section_n != virus_section_n:
            continue

        cnt = 0
        visit = [[False] * n for _ in range(n)]
        for x,y in q:
            visit[x][y] = True

        inactive = 0

        while q:
            length = len(q)
            b = False

            for _ in range(length):
                x,y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx == n or ny == n:
                        continue

                    if visit[nx][ny] == True or arr[nx][ny] == 1:
                        continue

                    if arr[nx][ny] == 0:
                        if b == False:
                            cnt += inactive
                        b = True

                    q.append([nx,ny])
                    visit[nx][ny] = True

            if b:
                cnt += 1
                inactive = 0
            else:
                inactive+= 1

        if cnt > 0:
            iRet = min(iRet, cnt)

    if iRet == 2500:
        iRet = -1

    return iRet

n,m = map(int,input().split())
arr = []    #0(빈칸) 1(벽) 2(바이러스)
for _ in range(n):
    arr.append(list(map(int,input().split())))

empty_section, empty_section_n = get_empty_section()

virus = get_virus()

all_virus_section_n = get_virus_section(virus)
if empty_section_n == 0:
    print(0)
elif empty_section_n != all_virus_section_n:
    print(-1)
else:
    print(solution())