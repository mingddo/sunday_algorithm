from collections import deque

def bfs():
    global cnt
    while start:
        x, y = start.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<= nx < N and 0<= ny < M and arr[nx][ny] == 0 and visited[nx][ny] == 0:
                start.append((nx,ny))
                arr[nx][ny] = 1
                visited[nx][ny] = visited[x][y] + 1

M, N = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
start = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*M for _ in range(N)]
valid = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            start.append((i,j))
            visited[i][j] = 1
        elif arr[i][j] == 0:
            valid = 1
if valid == 1:
    bfs()
    for ar in arr:
        if ar.count(0):
            result = -1
            break
        else:
            result = 0
            for v in visited:
                if result < max(v)-1:
                    result = max(v)-1

else:
    result = 0

print(result)