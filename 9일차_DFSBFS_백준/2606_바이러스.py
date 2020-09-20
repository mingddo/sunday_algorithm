import sys
sys.stdin = open("input.txt", "r")
def DFS(s):
    global cnt
    visited[s] = 1
    for i in range(N+1):
        if arr[s][i] == 1 and visited[i] == 0:
            cnt += 1
            DFS(i)
N = int(input())
M = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    r, c = map(int, input().split())
    arr[r][c] = arr[c][r] = 1
visited = [0]*(N+1)
cnt = 0
DFS(1)
print(cnt)