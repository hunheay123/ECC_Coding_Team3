from collections import deque

# 입력 받기
N, K = map(int, input().split())

# 큐 초기화 (1부터 N까지)
queue = deque([i for i in range(1, N + 1)])

result = []

# K번째 사람을 계속해서 제거
while queue:
    # K-1번 만큼 큐에서 뒤로 보내기
    queue.rotate(-(K-1))
    # K번째 사람 제거하고 결과에 추가
    result.append(queue.popleft())

# 결과 출력 (요세푸스 순열 출력)
print("<", end="")
print(", ".join(map(str, result)), end="")
print(">")
