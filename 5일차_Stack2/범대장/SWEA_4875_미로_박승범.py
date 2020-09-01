import sys
sys.stdin = open("input.txt", "r")

def search():
    st_row, st_col = 0, 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                st_row, st_col = i, j
                return st_row, st_col

def DFS(st_row, st_col):
    global N, result
    if arr[st_row][st_col] == 3:
        result = 1
        return
    visitied[st_row][st_col] = True
    for i in range(4):
        ddrr = st_row + dr[i]
        ddcc = st_col + dc[i]
        if ddrr < 0 or ddrr >= N or ddcc < 0 or ddcc >= N:
            continue
        elif visitied[ddrr][ddcc] == True or arr[ddrr][ddcc] == 1:
            continue
        DFS(ddrr, ddcc)

for t in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visitied = [[False]*N for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    result = 0
    st_row, st_col = search()
    DFS(st_row, st_col)
    if result == 1:
        print('#{} 1'.format(t))
    else:
        print('#{} 0'.format(t))