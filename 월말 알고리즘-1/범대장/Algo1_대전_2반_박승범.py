# 테스트 케이스 숫자를 입력 받음과 동시에 for문 실행
for t in range(1, 1+int(input())):
    # 배열 크기 N, 첫 번째 입력 값(M), 변경 값(D) 차례로 입력 받음
    N, M, D = map(int, input().split())
    # 숫자를 NxN 크기에 맞춰 생성하고 모든 수를 0으로 맞춤
    arr = [[0]*N for _ in range(N)]
    # N//2값은 M의 좌표가 될 수도 있고 이 후 계산에 많이 쓰이기 때문에 소문자n으로 저장
    n = N//2
    # NxN 배열의 가장 테두리 부터 색칠하여 안쪽으로 들어오는 방향으로 설계
    # 이에 a, b를 열,행의 값을 하나씩 줄여나가는데에 쓰임
    a, b = 0, 0
    # c는 배열의 크기인 N이 짝수 인지 홀수 인지에 따라 달라짐으로 1 혹은 0을 저장
    if N % 2 == 0:
        c = 1
    else:
        c = 0
    # 가장 안쪽 배열(가운데)로 왔을 때 즉 n = a or b 가 됬을때
    # while문 탈출하는 식으로 설계
    while True:
        for i in range(a, N-a):
            for j in range(b, N-b):
                #위에서 말했듯 가장 밖 테두리 부터 안쪽으로 들어오는 식
                arr[i][j] = M+(D*(n-c))
        # 하나씩 더해줘서 점점 안쪽으로 c는 값의 차이를 두기위한 변수
        a += 1
        b += 1
        c += 1
        # n = a or  b일 때 와일문 탈출 아니면 out of range 에러
        if a > n or b > n:
            break
    # 이 밑에는 출력예시에 따른 print 설계
    print(arr)
    print('#{}'.format(t), end=' ')
    for i in arr:
        print('{}'.format(sum(i)), end=' ')
    print()