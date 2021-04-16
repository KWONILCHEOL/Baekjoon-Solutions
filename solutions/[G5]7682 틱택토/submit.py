# [G5]7682 틱택토
# https://www.acmicpc.net/problem/7682

import sys
input = sys.stdin.readline

def check():
    for i in range(1,9):
        a,b,c = line[i]
        if arr[a] == arr[b] and arr[b] == arr[c]:
            if arr[a] != '.':
                temp.append(i)

line = [[],[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
line_type = [[],[1],[2],[3],[4],[5],[6],[7],[8],[1,4],[1,5],[1,6],[1,7],[1,8],[2,4],[2,5],[2,6],[2,7],[2,8],[3,4],[3,5],[3,6],[3,7],[3,8],[4,7],[4,8],[5,7],[5,8],[6,7],[6,8],[7,8]]
arr = ['.'] * 9

while True:
    arr = str("." + input().rstrip())
    if arr == ".end":
        break
    arr = list(arr)
    o_n = arr.count('O')
    x_n = arr.count('X')

    if x_n < o_n:
        print("invalid")
        continue

    if o_n + 2 <= x_n:
        print("invalid")
        continue

    temp = []
    check()
    if o_n + x_n < 9 and len(temp) == 0:
        print("invalid")
        continue

    if temp not in line_type:
        print("invalid")
        continue

    if len(temp) == 1:
        if arr[line[temp[0]][0]] == 'O' and o_n != x_n:
            print("invalid")
            continue

        if o_n == x_n and arr[line[temp[0]][0]] == 'X':
            print("invalid")
            continue

    if len(temp) == 2:
        if arr[line[temp[0]][0]] != arr[line[temp[1]][0]]:
            print("invalid")
            continue

    print("valid")