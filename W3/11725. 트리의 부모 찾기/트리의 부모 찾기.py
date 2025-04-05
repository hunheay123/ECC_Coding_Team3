import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

# 양방향 간선 입력
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# BFS로 부모 찾기
def bfs(start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for child in tree[node]:
            if parent[child] == 0:
                parent[child] = node
                queue.append(child)

# 루트는 1로 지정
bfs(1)

# 2번 노드부터 출력
for i in range(2, n + 1):
    print(parent[i])
