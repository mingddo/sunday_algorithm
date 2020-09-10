import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 1+int(input())):
    N, M, K = map(int, input().split())
    li = list(map(int, input().split()))
    num = 0
    insert_num = 0
    while K != 0:
        num += M
        num %= len(li)
        if num == 0:
            li.append(li[num-1] + li[0])
            num -= 1
        else:
            li.insert(num, li[num-1] + li[num])
        K -= 1
    print('#{}'.format(t), end=' ')
    print(*li[-1:-11:-1], end='')

        