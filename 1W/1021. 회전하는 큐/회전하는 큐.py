from collections import deque

# 입력 받기
N, M = map(int, input().split())  # 큐의 크기 N, 뽑아낼 원소의 개수 M
target = list(map(int, input().split()))  # 뽑아낼 원소들의 위치

# 큐 초기화
queue = deque([i for i in range(1, N + 1)])

# 연산 횟수 변수
count = 0

# 각 원소를 뽑을 때마다 수행할 작업
for t in target:
    # 큐에서 t의 인덱스를 찾는다
    idx = queue.index(t)
    
    # 왼쪽으로 이동하는 횟수와 오른쪽으로 이동하는 횟수를 구해 최소값을 선택
    if idx <= len(queue) // 2:
        # 왼쪽으로 이동하는 것이 더 빠름
        count += idx
        queue.rotate(-idx)  # 왼쪽으로 idx만큼 회전
    else:
        # 오른쪽으로 이동하는 것이 더 빠름
        count += len(queue) - idx
        queue.rotate(len(queue) - idx)  # 오른쪽으로 회전
    
    # 원소를 뽑고 제거
    queue.popleft()

# 결과 출력
print(count)
