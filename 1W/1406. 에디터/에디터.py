import sys
input = sys.stdin.read

def main():
    data = input().splitlines()
    
    # 초기 문자열
    initial_string = data[0]
    
    # 명령어 개수
    M = int(data[1])
    
    # 명령어들
    commands = data[2:]
    
    # 스택들
    left_stack = list(initial_string)  # 커서 왼쪽 부분
    right_stack = []  # 커서 오른쪽 부분
    
    # 명령어 처리
    for command in commands:
        if command == 'L':  # 커서 왼쪽으로 한 칸 옮김
            if left_stack:
                right_stack.append(left_stack.pop())
        elif command == 'D':  # 커서 오른쪽으로 한 칸 옮김
            if right_stack:
                left_stack.append(right_stack.pop())
        elif command == 'B':  # 커서 왼쪽의 문자 삭제
            if left_stack:
                left_stack.pop()
        else:  # P $ 명령어
            _, char = command.split()
            left_stack.append(char)
    
    # 결과 출력
    print(''.join(left_stack) + ''.join(reversed(right_stack)))

if __name__ == "__main__":
    main()
