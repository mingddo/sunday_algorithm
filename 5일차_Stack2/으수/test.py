#미로를 짜보쟈(DFS)
#1은 벽이고, 0이 길, 2는 출발점, 3은 도착점
#일단 배열을 입력받는다
#0을따라 계속 감, 가다가 1을 만나면 0인 곳으로 방향 전환(오,왼,아래,위 순서로 볼거야)/일단가는 방향을 우선시해줄거야!
#방문배열을 해서 그전에 갔던 곳은 가지 않게 함,,,근데 이러면 길이 아니라서 돌아갈때 오류가 생기지 않을까? 일단해본다
#다음 위치가 idx에 벗어나지 않는지 확인, 방문하지 않은 곳인지 확인
#종료조건은 3을 만나면 종료!, 아니면 더이상 갈곳이 없을때!
#시작점은 (1,1)이고 도착점(끝점)은(13,13)임
#도착했다는 것을 저장할 global변수 필요함(ans)


#역시나 방문배열을 쓰니 막혔을때 뒤로 못돌아감!
#이럴떄 어떻게 해야되는걸까
#그때 다시 리셋을 하고, 다시 기록하게 할까?

import sys
sys.stdin = open('inputpy.txt','r')

di = [0,0,1,-1] #오, 왼, 아, 위
dj = [1,-1,0,0]

def check(i,j):
    global ans
    visited[i][j] = True
    # print(i,j)
    #종료조건
    #idx 벗어나면 continue, 방문했던 곳이면 continue, maize[ni][nj]가 0이 아니면 continue,
    for d in range(4): #4방향을 볼거야
        ni = i + di[d]
        nj = j + dj[d]
        # if 0 <= ni < 16 and 0 <= nj < 16 and (maize[ni][nj] == 0 or maize[ni][nj] == 3) and visited[ni][nj] == False:
        #     check(ni, nj)
        if ni < 0 or ni >= 16 or nj < 0 or nj >= 16:
            continue
        if visited[ni][nj] == True:
            continue
        if maize[ni][nj] != 0:
            if maize[ni][nj] == 3:
                ans = 1
                return
            continue
        check(ni, nj)

        # if maize[ni][nj] == 0 or maize[ni][nj] == 3:
        #     check(ni, nj)

for tc in range(1,11):
    ans = 0 #초기화(tc돌때마다)
    T = int(input())
    maize = [list(map(int,input())) for _ in range(16)]
    # print(maize)
    # for i in range(16):
    visited = [[False for j in range(16)] for i in range(16)] #방문배열 초기화
    check(1,1)
    if ans == 1:
        print('#{} {}'.format(tc,ans))
    else: #못찾음
        print('#{} 0'.format(tc))