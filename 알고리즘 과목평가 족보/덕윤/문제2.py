import sys
sys.stdin = open("input(2).txt", "r")

def plus(k, plus_arr):
    result = 0
    for x in range(k):
        if x == 0 or x==k-1:
            result += sum(plus_arr[x])
        else:
            result += (plus_arr[x][0]+ plus_arr[x][k-1])
    compare.append(result)
    return


def box(x):
    for i in range(N-x+1):
        for j in range(M-x+1):
            k_arr = []
            for a in range(x):
                k_arr.append(arr[i+a][j: j+x])
            plus(x, k_arr)
    return

for tc in range(1, int(input()) + 1):
    N, M, k = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    compare = []
    box(k)
    print('#{} {}'.format(tc, max(compare)))