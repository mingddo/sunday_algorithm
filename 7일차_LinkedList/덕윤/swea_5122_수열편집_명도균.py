import sys

sys.stdin = open("input (2).txt", "r")

for test_case in range(1, int(input()) + 1):
    N, M, L = map(int,input().split())
    arr = list(map(int,input().split()))
    for _ in range(M):
        k = list(input().split())
        if k[0] == 'I':
            a = int(k[1])
            b = int(k[2])
            arr = arr[:a]+ [b] + arr[a:]
        elif k[0] == 'D':
            arr.pop(int(k[1]))
        else:
            arr[int(k[1])] = int(k[2])

    try:
        result = arr[L]
    except:
        result = -1

    print('#{} {}'.format(test_case,result))