import sys
sys.stdin = open('5110.txt', 'r')

for t in range(1, 1+int(input())):
    print('#{}'.format(t), end=' ')
    N, M = map(int, input().split())
    first_li = list(map(int, input().split()))
    for m in range(M-1):
        next_li = list(map(int, input().split()))
        for i in range(len(first_li)):
            if first_li[i] > next_li[0]:
                for j in range(N):
                    first_li.insert(i+j, next_li[j])
                break
        else:
            first_li.extend(next_li)
    for i in range(1,11):
        print('{}'.format(first_li[-i]), end=' ')
    print()