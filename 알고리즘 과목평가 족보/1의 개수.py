
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
#input
# 7
# 0000011
# 0000000
# 0011100
# 0010111
# 0110010
# 0011100
# 0000000


# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def DFS(r, c):
    #개수를 위한 글로벌 선언
    global cnt
    #요기 왔다는건 1이라는 뜻이므로 카운트 증가
    arr[r][c] = 0
    cnt += 1

    #4방향 탐색
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        #범위를 벗어나면 out, 다음좌표가 0이라면 out
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if arr[nr][nc] == 0:
            continue
        #위에 다걸리지 않았다면 다음좌표도 1이고 맵의 크기도 안벗어난 것이므로 재귀
        DFS(nr, nc)


N = int(input())

arr = [list(map(int, input())) for _ in range(N)]

#2차원 순회하면서 1인 좌표부터 DFS 시작
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            #개수를 매번 새로 세야하기 때문에 초기화
            cnt = 0
            DFS(i, j)
            print(cnt)
