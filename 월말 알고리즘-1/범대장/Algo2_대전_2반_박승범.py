# DFS 알고리즘 기법사용
# 물고기의 이동은 상하좌우, 즉 마당이 상하좌우로 묶여 있는 집단을 찾아
# 개수를 반환하는 문제

# DFS 함수에서는 main에서 보내준 행, 열값에 해당하는 arr을 0으로 전환
# 이미 물고기를 배치한 곳의 흑적을 삭제한다는 뜻
def DFS(r, c):
    arr[r][c] = 0
    # 방향 상하좌우 모두 검색
    for i in range(4):
        new_r = r + dr[i]
        new_c = c + dc[i]
        # 연못의 범위를 벗어나면 패스 = 마당으로 나오면 패스
        if new_r < 0 or new_c < 0 or new_r >= N or new_c >=M:
            continue
        # 이미 물고기가 배치된 연못이여도 패스
        elif arr[new_r][new_c] == 0:
            continue
        # 이외에 해당하는 경우는 DFS함수를 재귀하여 반복
        DFS(new_r, new_c)

# tast case를 받음과 동시에 for문 실행
for t in range(1, 1+int(input())):
    # 마당 총 가로 M, 세로 N, 좌표 개수 K
    M, N, K = map(int, input().split())
    # 마당 가로 세로에 해당하는 arr 배열 생성
    arr = [[0]*M for _ in range(N)]
    # 좌표를 for문으로 받아 0을 1로 전환
    for _ in range(K):
        m, n = map(int, input().split())
        arr[n][m] = 1
    # DFS 함수에서 delta 이동시 도움을 주는 배열 dr, dc
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 연결된 연못의 수를 새우기 위함 연못의 수는 곧 배치될 물고기의 수
    cnt = 0
    for i in range(N):
        for j in range(M):
            # 연못을 찾으면 연결된 좌표를 다 찾는 DFS로 인자전달
            # cnt에 +1
            if arr[i][j] == 1:
                DFS(i, j)
                cnt += 1
    # 출력
    print('#{} {}'.format(t, cnt))