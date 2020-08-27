def abba(lst):
    tmp = []
    l = len(lst)
    for i in range(l):
        if lst[i] == lst[-i - 1]:
            tmp.append(lst[i])
            if len(tmp) == (l):
                return tmp
        else:
            tmp = []

T = int(input())
for test_case in range(1, T + 1):
    print('#{} '.format(test_case), end="")
    N, M = map(int, input().split())
    arrs = [list(input()) for _ in range(N)]

    # r행 수집
    for r in range(N):
        for c in range(N - M + 1):
            if abba(arrs[r][c:c + M]):
                print(''.join(abba(arrs[r][c:c + M])))

    # c열 수집
    col = []
    cols = []
    for i in range(N - M + 1):
        for j in range(N):
            if len(col) == M:
                cols.append(col)
                col = []
            for n in range(0, M):
                col.append(arrs[i + n][j])
    for c in cols:
        if abba(c):
            print(''.join(c))
