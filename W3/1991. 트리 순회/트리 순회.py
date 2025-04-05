class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node].left)
    preorder(tree[node].right)

def inorder(node):
    if node == '.':
        return
    inorder(tree[node].left)
    print(node, end='')
    inorder(tree[node].right)

def postorder(node):
    if node == '.':
        return
    postorder(tree[node].left)
    postorder(tree[node].right)
    print(node, end='')

# 트리 저장 딕셔너리
tree = {}

# 입력 처리
n = int(input())
for _ in range(n):
    root, left, right = input().split()
    tree[root] = Node(left, right)

# 순회 출력
preorder('A')   # 전위 순회
print()
inorder('A')    # 중위 순회
print()
postorder('A')  # 후위 순회


ㅇ
