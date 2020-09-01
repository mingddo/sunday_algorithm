import sys
sys.stdin = open("input.txt", "r")
# backtracking을 모른다고 가정하고 짠 알고리즘
# 내일 교수님 수업 들으면서 좀 더 최적화 해보기

def backtracking(ii, summ):
    global minn
    if ii >= N:
        minn = summ
        return
    for j in range(N):
        summm = summ + arr[ii][j]
        if  j in visited[:ii]:
            continue
        elif summm >= minn:
            continue
        visited[ii] = j
        iii = ii + 1
        backtracking(iii, summm)

for t in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    minn = 0
    # 문제에서 나올 수 있는 max 값을 초기 minn값으로 설정
    for i in range(N):
        minn += max(arr[i])
    backtracking(0, 0)
    print('#{} {}'.format(t, minn))