# [S1]12849 본대산책
# https://www.acmicpc.net/problem/12849

#[0] = sum([1,2])
#[1] = sum([0,2,3])
#[2] = sum([0,1,3,5])
#[3] = sum([1,2,4,5])
#[4] = sum([3,5,6])
#[5] = sum([2,3,4,7])
#[6] = sum([4,7])
#[7] = sum([5,6])

import sys
input = sys.stdin.readline

d = int(input())
arr = [1,0,0,0,0,0,0,0]

for i in range(1, d+1):
    temp = [0] * 8
    temp[0] = (arr[1] + arr[2]) % 1000000007
    temp[1] = (arr[0] + arr[2] + arr[3]) % 1000000007
    temp[2] = (arr[0] + arr[1] + arr[3] + arr[5]) % 1000000007
    temp[3] = (arr[1] + arr[2] + arr[4] + arr[5]) % 1000000007
    temp[4] = (arr[3] + arr[5] + arr[6]) % 1000000007
    temp[5] = (arr[2] + arr[3] + arr[4] + arr[7]) % 1000000007
    temp[6] = (arr[4] + arr[7]) % 1000000007
    temp[7] = (arr[5] + arr[6]) % 1000000007
    arr = temp

print(arr[0])