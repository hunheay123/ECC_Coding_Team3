import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

# 입력 처리
for _ in range(V):
    temp = list(map(int, input().split()))
    node = temp[0]
    idx = 1
    while temp[idx] != -1:
        graph[node].append((temp[idx], temp[idx + 1]))
        idx += 2

# DFS 함수
def dfs(node, dist):
    for next_node, weight in graph[node]:
        if visited[next_node] == -1:
            visited[next_node] = dist + weight
            dfs(next_node, dist + weight)

# 첫 DFS: 임의의 노드(1)에서 가장 먼 노드 찾기
visited = [-1] * (V + 1)
visited[1] = 0
dfs(1, 0)

farthest_node = visited.index(max(visited))

# 두 번째 DFS: 그 노드에서 가장 먼 거리 찾기
visited = [-1] * (V + 1)
visited[farthest_node] = 0
dfs(farthest_node, 0)

print(max(visited))



