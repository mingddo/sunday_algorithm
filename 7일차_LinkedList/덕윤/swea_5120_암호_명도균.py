import sys

sys.stdin = open("input(1).txt", "r")
def f(m, k):
    i = 0
    while k != 0:
        i += m
        if i < len(arr):
            arr[i:i] = [arr[i-1] + arr[i]]
            k -= 1
        elif i == len(arr):
            arr.append(arr[0]+arr[len(arr)-1])
            i = -1
            k -= 1
        else:
            i = i % len(arr)
            arr[i:i] = [arr[i - 1] + arr[i]]
            k -= 1


for test_case in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int,input().split()))
    f(M,K)
    if len(arr) > 10:
        password = arr[len(arr)-1:len(arr)-11:-1]
    else:
        password = arr[::-1]
    print('#{}'.format(test_case),end=' ')
    print(*password)