# [G5]2493 탑
# https://www.acmicpc.net/problem/2493

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int,input().split()))
result = [0] * (n+1)

st = deque()
st.append((arr[n], n))
for i in range(n-1, 0, -1):
    x = arr[i]
    while st.__len__() > 0 and x >= st[0][0]:
        result[st[0][1]] = i
        st.popleft()
    st.appendleft((x,i))

print(*result[1:])