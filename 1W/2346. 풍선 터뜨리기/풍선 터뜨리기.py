from collections import deque

# 입력 받기
N = int(input())  # 풍선의 개수
balloons = list(map(int, input().split()))  # 각 풍선에 적힌 숫자

# 풍선 번호와 그 번호에 해당하는 값을 함께 넣어둔 큐
queue = deque([(i+1, balloons[i]) for i in range(N)])

# 결과를 저장할 리스트
result = []

# 첫 번째 풍선 터뜨리기
while queue:
    # 큐에서 가장 앞의 풍선 꺼내기
    num, move = queue.popleft()
    result.append(num)
    
    # 해당 숫자만큼 이동하기
    if len(queue) > 0:  # 남은 풍선이 있을 경우만 이동
        if move > 0:  # 양수일 경우 오른쪽으로
            queue.rotate(-(move - 1))
        else:  # 음수일 경우 왼쪽으로
            queue.rotate(-move)

# 결과 출력
print(*result)
