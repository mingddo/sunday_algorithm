import sys
sys.stdin = open("input.txt", "r")

def DFS(r, c):
    global cnt
    visited[r][c] = 1
    if r == N-1 and c == M-1:
        result.append(cnt)
        return
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0 <= rr < N and 0 <= cc < M and visited[rr][cc] == 0 and arr[rr][cc] == 1:
            DFS(rr, cc)
            cnt += 1
# main
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
result = []
cnt = 0
DFS(0, 0)
print(result)