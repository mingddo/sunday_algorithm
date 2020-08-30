import sys
sys.stdin = open('문제3.txt', 'r')

def dfs(x, y, N):
    visited.append((x, y))
    for a, b in delta:
        nx = a + x
        ny = b + y
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if (nx, ny) in visited:
            continue
        if not arr[nx][ny]:
            continue
        dfs(nx, ny, N)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [[int(x) for x in input().split()] for _ in range(N)]
    delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    visited = []
    res = 0
    for i in range(N):
        for j in range(N):
            if (i, j) not in visited and arr[i][j]:
                res += 1
                dfs(i, j, N)
    print('#{} {}'.format(tc, res))