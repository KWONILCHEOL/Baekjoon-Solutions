# [G4]1647 도시 분할 계획
# https://www.acmicpc.net/problem/1647
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    while parent[x] != x:
        parent[x], x = parent[parent[x]], parent[x]
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
P = [i for i  in range(v+1)]

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(P, a) != find_parent(P, b):
        union_parent(P, a, b)
        result += cost
        last = cost

print(result - last)

# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4
