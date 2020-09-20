import sys
sys.stdin = open("input.txt", "r")


def DFSdelta(r, c):
    arr[r][c] = 0
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0 <= rr < M and 0 <= cc < N and arr[rr][cc] == 1:
            DFSdelta(rr, cc)
for _ in range(int(input())):
    M, N, K = map(int, input().split())
    arr = [[0]*N for _ in range(M)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    cnt = 0
    for _ in range(K):
        r, c = map(int, input().split())
        arr[r][c] = 1
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
                DFSdelta(i, j)
    print(cnt)