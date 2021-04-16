import sys
input = sys.stdin.readline

n = int(input())
d = [[0] * (n+1) for _ in range(n+1)]
a = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    d[i][i] = 1
    if a[i-1] == a[i]:
        d[i-1][i] = 1

#k = i부터 j까지 길이
#d[i + 1][j - 1] = i+1부터 j-1까지 팰린드롬 여부
for k in range(3, n+1):
    for i in range(1, n - k + 1 + 1):
        j = i + k - 1
        if a[i] == a[j] and d[i + 1][j - 1]:
            d[i][j] = 1

m = int(input())
for _ in range(m):
    x, y = map(int,input().split())
    print(d[x][y])