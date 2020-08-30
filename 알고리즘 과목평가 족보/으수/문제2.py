import sys
sys.stdin = open("문제2.txt", "r")

def sum1(K):
    result = 0
    for x in range(K):
        for y in range(K):
            if x == 0 or x == K - 1:
                result += arr[i + x][j + y]
            else:
                if 0 < y < K-1:
                    continue
                result += arr[i + x][j + y]
    return result

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    arr = [[int(x) for x in input().split()] for _ in range(N)]
    res = []
    for i in range(N-K+1):
        for j in range(M-K+1):
            res.append(sum1(K))
    print('#{} {}'.format(tc, max(res)))