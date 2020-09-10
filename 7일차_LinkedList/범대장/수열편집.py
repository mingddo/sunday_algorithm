import sys
sys.stdin = open("input.txt", "r")

for t in range(1,1+int(input())):
    N, M, L = map(int, input().split())
    li = list(map(int, input().split()))
    for _ in range(M):
        plus = list(input().split())
        if plus[0] == 'I':
            li.insert(int(plus[1]), int(plus[2]))
        elif plus[0] == 'D':
            li.pop(int(plus[1]))
        elif plus[0] == 'C':
            li[int(plus[1])] = int(plus[2])
    if len(li) <= L:
        print('#{} -1'.format(t))
    else:
        print('#{} {}'.format(t, li[L]))