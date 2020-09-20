import sys
#sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N = int(input())
    number = [0] + list(map(int,input().split()))
    tree = [0] * (N+1)
    cnt = 0
    for i in range(1,N+1):
        tree[i] = number[i]
        if i > 1:
            while True:
                if tree[i//2] > tree[i]:
                    tree[i//2], tree[i] = tree[i], tree[i//2]
                    if i//2 == 1:
                        break
                    else:
                        i = i//2
                else:
                    break
    while N != 1:
        N = N//2
        cnt += tree[N]
    print('#{} {}'.format(test_case,cnt))
