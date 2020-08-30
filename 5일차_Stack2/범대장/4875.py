import sys
sys.stdin = open("input.txt", "r")

# visited를 쓰면 다른 길을 찾을 수가 없음
def search():
    st_row, st_col, en_row, en_col = 0, 0, 0, 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                st_row, st_col = i, j
            elif arr[i][j] == 3:
                en_row, en_col = i, j
    return st_row, st_col, en_row, en_col

def DFS(st_row, st_col):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visitied[st_row][st_col] = True
    for i in range(4):
        ddrr = st_row + dr[i]
        ddcc = st_col + dc[i]
        if arr[ddrr][ddcc] == 0 and 0 <= ddrr < len(visitied) and 0 <= ddcc < len(visitied) and visitied[ddrr][ddcc] == False:
            return DFS(ddrr,ddcc)
        elif arr[ddrr][ddcc] == 3:
            return 1
    else:
        return 0

for t in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visitied = [[False]*N for _ in range(N)]
    st_row, st_col, en_row, en_col = search()
    result = DFS(st_row, st_col)
    print('#{} {}'.format(t, result))