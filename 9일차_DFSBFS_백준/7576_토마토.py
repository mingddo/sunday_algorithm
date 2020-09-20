import sys
sys.stdin = open("input.txt", "r")

from collections import deque
# main
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
startpoint = deque()
q = deque()
cnt = -1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            startpoint.append((i, j))
while startpoint:
    r, c = startpoint.popleft()
    visited[r][c] = 1
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0 <= rr < N and 0 <= cc < M and arr[rr][cc] == 0 and visited[rr][cc] == 0:
            arr[rr][cc] = 1
            q.append((rr, cc))
            visited[rr][cc] = 1
    if len(startpoint) == 0:
        cnt += 1
        startpoint += q
        q =[]
for n in range(N):
    if 0 in arr[n]:
        print(-1)
        break
else:
    print(cnt)