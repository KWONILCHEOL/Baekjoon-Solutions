# [S3]14889 스타트와 링크
# https://www.acmicpc.net/problem/14889

import sys
input = sys.stdin.readline

def check():
    score1 = 0
    score2 = 0

    for i in range(n//2):
        for j in range(i+1, n//2):
            score1 += A[team1[i]][team1[j]]
            score2 += A[team2[i]][team2[j]]

    global answer
    answer = min(answer, abs(score1 - score2))

def go(cur):
    if cur == n:
        check()
        return

    if len(team1) == n//2:
        team2.append(cur)
        go(cur + 1)
        team2.remove(cur)
    elif len(team2) == n//2:
        team1.append(cur)
        go(cur + 1)
        team1.remove(cur)
    else:
        team1.append(cur)
        go(cur + 1)
        team1.remove(cur)

        team2.append(cur)
        go(cur + 1)
        team2.remove(cur)

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        A[i][j] += A[j][i]

team1 = []
team2 = []
answer = 1e19
go(0)
print(answer)