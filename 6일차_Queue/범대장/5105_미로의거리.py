def BFS(ii, jj):
    q = []
    q.append((ii, jj))
    visited[ii][jj] = 0
    while len(q):
        r, c = q.pop(0)
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if 0 <= rr < N and 0 <= cc < N and visited[rr][cc] == False and arr[rr][cc] == 0:
                q.append((rr,cc))
                visited[rr][cc] = visited[r][c] + 1
            elif 0 <= rr < N and 0 <= cc < N and visited[rr][cc] == False and arr[rr][cc] == 3:
                return visited[r][c]
    return 0

def search():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

for t in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    ii, jj = search()
    result = BFS(ii, jj)
    print('#{} {}'.format(t, result))