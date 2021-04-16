# [G4]1082 방 번호
# https://www.acmicpc.net/problem/1082

import sys
input = sys.stdin.readline

n = int(input())
price = list(map(int,input().split()))
price_len = len(price)
money = int(input())

dp = [('') for _ in range(money+1)]

for i in range(money+1):
    for j in range(price_len):
        if price[j] <= i:
            if len(dp[i]) > len(dp[i-price[j]] + str(j)):
                continue
            elif len(dp[i-price[j]] + str(j)) == [dp[i-price[j]] + str(j)].count('0'):
                continue
            elif len(dp[i]) < len(dp[i-price[j]] + str(j)):
                dp[i] = dp[i - price[j]] + str(j)
            elif sorted(dp[i], reverse=True) < sorted(dp[i - price[j]] + str(j), reverse=True):
                dp[i] = dp[i - price[j]] + str(j)

print(dp[money] if dp[money] != "" else 0)