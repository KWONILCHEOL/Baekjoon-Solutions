# [G2]2623 음악프로그램
# https://www.acmicpc.net/problem/2623

# 위상정렬
# if indegree[x] == 0 : arr.append(x)
# if len(arr) != n : print(0)
# else : print(*arr, sep='\n')

import sys
import heapq
input = sys.stdin.readline