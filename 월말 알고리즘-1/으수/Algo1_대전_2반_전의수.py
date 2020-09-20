import sys
sys.stdin = open('Algo1.txt', 'r')

# 테두리에 값을 넣는 함수
def coloring(x, y, e):
    for i in range(x, N-x): # 시작점이 계속 바뀌기 때문에 range의 범위도 x,y입력받은 형태로 시작해야한다.
        for j in range(y, N-y): # 또한 끝좌표도 계속 1씩 줄어들기 때문에 N-y 형태로 해준다.
            # 테두리에 값을 입력받는 부분
            if i == x or i == (N-x-1): # 가장 첫줄과 가장 마지막줄에는 다 값을 넣는다
                arr[i][j] = e
            elif j == y or j == (N-y-1): # 첫줄과 마지막줄이 아닌 부분에는 첫열과 마지막열에만 값을 넣는다
                arr[i][j] = e

# 테스트 케이스 입력받기
T = int(input())

# 테스트 케이스를 반복문 돌리는 부분
for tc in range(1, T+1):

    # 입력과 초기화 부분
    N, M, D = map(int, input().split()) # N, M, D의 값을 입력받기
    arr = [[0] * N for _ in range(N)] # N*N이 0으로 채워진 배열 초기화
    end = M + (N // 2) * D # 가장 끝 테두리에 들어갈 숫자를 계산한 식을 end에 저장
    arr[N//2][N//2] = M # 가장 중심부분(M)에 값을 칠하는 식

    # 값을 저장하는 함수를 반복하는 부분
    for i in range(N//2): # 테두리 안쪽으로 파고들면서 컬러링 함수를 통해 각각의 변수 저장
        coloring(i, i, end) # i가 0, 1, 2... 이런식으로 변하기 떄문에 컬러링 함수에 좌표를 넘겨준다(0, 0), (1, 1)과 같은형태
        end -= D # 가장테두리에서 안쪽으로 파고들때마다 -D씩 변하기 때문에 값을 변화시켜준다.

    # 출력부분
    print('#{}'.format(tc), end=' ') # 테스트케이스를 출력
    for i in range(N): # 각 행 반복
        print(sum(arr[i]), end=' ') #각 행을 차례로 출력
    print() # 출력형식을 맞추기 위해 한칸 띄우는 부분
