#상, 하, 좌, 우 검색하고 연못이 있고(1이고) and 방문하지 않았으면 이동해서 다시 검사하기.
def dfs(x,y):
    visited.append((x,y))
    for d in range(4):
        new_x = x + d_x[d]
        new_y = y + d_y[d]
        if 0 <= new_x < M and 0 <= new_y < N and pond[new_x][new_y] == 1 and (new_x, new_y) not in visited:
            dfs(new_x, new_y)



# 0으로 채워진 이차배열 초기화 후 연못 개수와 좌표를 받아서 1로 바꾸기.
for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    pond = [[0]*N for _ in range(M)]
    #입력받는 좌표가 가로좌표 열 먼저 행 나중임으로 이를 주의해서 입력받는다.
    for _ in range(K):
        b, a = map(int,input().split())
        pond[a][b] = 1
    # 연못이 연결되었는지 여부는 위, 아래 양옆(오른쪽, 왼쪽)이 연결되어있는지 여부이다.
    # dfs 함수를 통해 연결된 연못을 센다.
    # 이 때 이미 방문한 연못은 visited에 저장하고 세지 않는다.
    visited = []
    #상, 하, 좌, 우 델타이동 하기
    d_x = [0, 0, 1, -1]
    d_y = [-1, 1, 0, 0]
    #물고기 수
    cnt = 0
    #배열을 돌면서 1이면서 방문하지 않은 연못이 있다면 함수 호출해서 이어진 연못이 있는지 체크
    # 체크가 끝나면 cnt += 1 해줌(물고기 수)
    for c in range(M):
        for d in range(N):
            if pond[c][d] == 1 and (c,d) not in visited:
                dfs(c,d)
                cnt += 1

    print('#{} {}'.format(tc, cnt))