import sys
sys.stdin = open("input(3).txt", "r")

def dfs(x,y):
    global cnt
    for d in range(8):
        visited.append((x,y))
        dx = x + d_x[d]
        dy = y + d_y[d]
        if 0 <= dx < N and 0 <= dy < N and arr[dx][dy] != 0 and (dx,dy) not in visited:
            dfs(dx,dy)
    return


for tc in range(1, int(input())+1):
    N  = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    d_x = [0,0,-1,1,-1,1,-1,1]
    d_y = [-1,1,0,0,-1,-1,1,1]
    cnt = 0
    visited = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and (i,j) not in visited:
                dfs(i,j)
                cnt += 1
    print('#{} {}'.format(tc, cnt))