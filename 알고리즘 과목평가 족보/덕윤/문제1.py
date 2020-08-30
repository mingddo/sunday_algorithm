import sys
sys.stdin = open("input(1).txt", "r")
#칠해진 영역은 1 안칠해진 영역은 0으로 표시.
# 영역 이중배열 0 으로 초기화
# M 만큼 칠하니깐 for 문으로 반복,

#칠하는 함수 작성. 만약 1인 경우는 pass 혹은 그냥 1로 칠해도 상관 없음.
def paint(s_x,s_y,e_x,e_y):
        global arr
        for i in range(s_x-1,e_x):
            for j in range(s_y-1, e_y):
                arr[i][j] = 1
        return


for tc in range(1, int(input()) +1):
    N, M = map(int, input().split())
    arr = [[0]* N for _ in range(N)]
    for m in range(M):
        start_x, start_y, end_x, end_y = map(int,input().split())
        paint(start_x, start_y, end_x, end_y)
    cnt = 0
    for a in arr:
        cnt += a.count(1)

    print('#{} {}'.format(tc,cnt))