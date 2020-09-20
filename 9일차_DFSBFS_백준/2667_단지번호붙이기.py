import sys
sys.stdin = open("input.txt", "r")

def DFSdelta(r, c):
    global count
    arr[r][c] = 0
    count += 1
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0 <= rr < N and 0 <= cc < N and arr[rr][cc] == 1:
            DFSdelta(rr, cc)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt = 0
ccnt = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            count = 0
            cnt += 1
            DFSdelta(i, j)
            ccnt.append(count)
print(cnt)
for i in sorted(ccnt):
    print(i)

