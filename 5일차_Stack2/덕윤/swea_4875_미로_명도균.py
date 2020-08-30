
import sys

sys.stdin = open("input.txt", "r")
def dfs(x,y):
    global result
    for d in range(4):
        dx,dy = delta[d]
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < N and 0 <= new_y < N and arr[new_x][new_y] != 1:
            if arr[new_x][new_y] == 3:
                result = 1
                return
            arr[new_x][new_y] = 1
            dfs(new_x,new_y)

for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_x = i
                start_y = j
                break
    delta=[[0,-1],[-1, 0],[0,1],[1,0]]
    result = 0
    dfs(start_x, start_y)
    print('#{} {}'.format(test_case, result))