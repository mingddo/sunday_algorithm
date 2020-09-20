# 숫자 채우는 함수, 만약 채우려는 곳이 False인 경우에만 채워넣기
def full(x,y):
    global k
    for i in range(k):
        for j in range(k):
            if not arr[x+i][y+j]:
                arr[x+i][y+j] = M
    return


for tc in range(1, int(input())+1):
    N, M, D = map(int, input().split())
    # 입력 받은 N만큼 0으로 채워져 있는 초기 이중 배열 만들기
    arr = [[False]*N for _ in range(N)]
    # 가장 중앙 부터 1,3,5,7, ..... 개의 행렬에서 안채워진 부분만 숫차를 채우는 규칙을 가짐.
    # 시작 좌표는 가장 정 중앙.
    start_x, start_y = N//2, N//2
    k = 1
    for a in range(N//2 +1):
        # 함수 호출하고 끝나면 M바꿔주고 k도 바꿔주고
        full(start_x, start_y)
        #함수를 실행한 후에는 k,M,시작점 조정해주기.
        k += 2
        M = M + D
        start_x -= 1
        start_y -= 1
    # 다 채웠으면 행별로 합 구해서 result 리스트에 더하고 출력하기.
    result = []
    print('#{}'.format(tc),end=' ')
    for ar in arr:
        result.append(sum(ar))
    print(*result)