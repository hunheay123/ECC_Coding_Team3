from collections import deque

def main():
    N, M = map(int, input().split())
    maze = [list(map(int, list(input().strip()))) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and maze[nx][ny]==1 and visited[nx][ny]==0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    print(visited[N-1][M-1])

if __name__ == "__main__":
    main()