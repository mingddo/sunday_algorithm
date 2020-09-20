def bfs(a,b):
    q = []
    q.append((a,b))
    visited[a][b] = 1
    while q:
        x, y = q.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<= nx < N and 0<= ny < M and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1




N, M = map(int, input().split())

arr = [list(map(int,input())) for _ in range(N)]

#시작점 0,0 도착점: N-1, M-1
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*M for _ in range(N)]
bfs(0,0)

print(visited[N-1][M-1])