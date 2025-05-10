from collections import deque

def main():
    M, N, H = map(int, input().split())
    box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    queue = deque()

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m] == 1:
                    queue.append((h, n, m))

    directions = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

    while queue:
        z, x, y = queue.popleft()
        for dz, dx, dy in directions:
            nz, nx, ny = z+dz, x+dx, y+dy
            if 0<=nz<H and 0<=nx<N and 0<=ny<M and box[nz][nx][ny]==0:
                box[nz][nx][ny] = box[z][x][y] + 1
                queue.append((nz, nx, ny))

    result = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m] == 0:
                    print(-1)
                    return
                result = max(result, box[h][n][m])
    print(result - 1)

if __name__ == "__main__":
    main()