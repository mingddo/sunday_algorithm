import sys
sys.stdin = open("input (1).txt", "r")

def min_plus(x):
    global min_num
    global plus    #돌다가 지금 min값보다 커지면 할 필요 없음
    if min_num < plus:
        return #끝까지 갔을 때 값 비교 후 저장하기
    if x == N:
        if min_num > plus:
            min_num = plus
    for y in range(N):
        if idx[y] == 0:
            idx[y] = 1
            plus += numbers[x][y]
            min_plus(x+1)
            idx[y] = 0
            plus -= numbers[x][y]



for tc in range(1, int(input()) + 1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    plus = 0
    min_num = 1 << 32
    a = 1
    idx = [0] * N
    min_plus(0)

    print('#{} {}'.format(tc, min_num))