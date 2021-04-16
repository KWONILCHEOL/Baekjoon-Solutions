# [G1]2098 외판원 순회
# https://www.acmicpc.net/problem/2098
# [py]https://suri78.tistory.com/208
# [c+]https://m.blog.naver.com/PostView.nhn?blogId=kks227&logNo=220557403491

# 시작점을 어디로 해도 상관없음
# (0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 0) == (3 -> 4 -> 5 -> 0 -> 1 -> 2 -> 3)

import sys
input = sys.stdin.readline
INF = int(1e9)

def TSP(x, bit):
    if bit == end:
        return W[x][0] if W[x][0] > 0 else INF
    if dp[x][bit] > 0:
        return dp[x][bit]

    dp[x][bit] = INF
    for i in range(1, n):
        if bit & (1 << i) or W[x][i] == 0:
            continue
        dp[x][bit] = min(dp[x][bit], W[x][i] + TSP(i, (bit|(1<<i))))

    return dp[x][bit]

n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (1 << n)  for _ in range(n)]
end = (1<<n) - 1
print(TSP(0, 1))