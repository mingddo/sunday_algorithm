import sys
sys.stdin = open("input.txt", "r")

from collections import deque
# main
M, N, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N*H)]
visited = []
dr = [-1, 1, 0, 0, N, -N]
dc = [0, 0, 1, -1, 0, 0]
startpoint = deque()
q = deque()
cnt = -1
# 가장 처음 익은 토마토(1) 지점을 확인
for n in range(N*H):
    for m in range(M):
        if arr[n][m] == 1:
            startpoint.append((n, m))
# 익히기 시작
while startpoint:
    r, c = startpoint.popleft()
    visited.append((r, c))
    # 상자 내 상하좌우 확인
    for i in range(6):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0 <= rr < N*H and 0 <= cc < M and arr[rr][cc] == 0 and (rr, cc) not in visited:
            arr[rr][cc] = 1
            q.append((rr, cc))
            visited.append((rr, cc))
    # cnt += 1을 하기 위함
    if len(startpoint) == 0:
        cnt += 1
        startpoint += q
        q = deque()
# -1 check
for n in range(N*H):
    if 0 in arr[n]:
        print(-1)
        break
else:
    print(cnt)
