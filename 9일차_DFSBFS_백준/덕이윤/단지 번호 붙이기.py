def dfs(x,y):
    global h_cnt
    visited.append((x,y))
    h_cnt += 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<= nx < N and 0<= ny < N and arr[nx][ny] == 1 and (nx,ny) not in visited:
            dfs(nx,ny)

N = int(input())
house = 0
cnt = []
arr = [list(map(int,input())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visited = []

for a in range(N):
    for b in range(N):
        if arr[a][b] == 1 and (a,b) not in visited:
            house += 1
            h_cnt = 0
            dfs(a,b)
            cnt.append(h_cnt)
print(house)
for c in sorted(cnt):
    print(c)
