## 테스트케이스 10개 중 5개 오답..........^^^^^

def IsRoute(r,c):
    check = miro[r][c]
    if check != 1:  # 벽-1
        return True

def DFS(hr, hc):
    global result
    visited.append((hr, hc))  # 일단 저장

    for i in range(4):
        tr = hr + dr[i]  # here to there
        tc = hc + dc[i]
        if miro[tr][tc] == 3:
            result = 1
            break
        if IsRoute(tr, tc) and ((tr, tc) not in visited):
            DFS(tr, tc)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # 0-통로 ; 1-벽 ; 2-출발 ; 3-도착
    # 1-벽 패딩 입히기 (4군데)
    miro = [0] * (N + 2)
    miro[0] = [1] * (N + 2)
    miro[N+1] = [1] * (N + 2)
    for i in range(1, N+1):
        miro[i] = [1] + list(map(int, list(input()))) + [1]

    # <-, up, ->, down
    dr = [0, -1, 0, +1]
    dc = [-1, 0, +1, 0]

    # 초기 설정
    visited = []  # (주의) DFS에 만들면 축적이 안됨
    result = 0

    # 시작점 찾기
    if 2 in miro[N]:
        start = miro[N].index(2)
        DFS(N, start)

    print('#{} {}'.format(test_case, result))

