import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
tree = {}
parent = [0] * (n + 1)

# 노드 정보 저장
for _ in range(n):
    node, left, right = map(int, input().split())
    tree[node] = (left, right)
    if left != -1:
        parent[left] = node
    if right != -1:
        parent[right] = node

# 루트 찾기 (부모가 없는 노드)
root = 0
for i in range(1, n + 1):
    if parent[i] == 0:
        root = i
        break

# 중위 순회하며 열 위치 기록
x = 1
level_min = {}
level_max = {}

def inorder(node, level):
    global x
    if node == -1:
        return
    left, right = tree[node]
    inorder(left, level + 1)

    # 열 위치 기록
    if level not in level_min:
        level_min[level] = x
        level_max[level] = x
    else:
        level_min[level] = min(level_min[level], x)
        level_max[level] = max(level_max[level], x)
    x += 1

    inorder(right, level + 1)

inorder(root, 1)

# 가장 넓은 레벨 찾기
max_width = 0
answer_level = 0
for level in level_min:
    width = level_max[level] - level_min[level] + 1
    if width > max_width:
        max_width = width
        answer_level = level
    elif width == max_width:
        answer_level = min(answer_level, level)

print(answer_level, max_width)
