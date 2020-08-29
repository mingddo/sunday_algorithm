## 이거 안돌아감,,,좀바꾸자

import sys
sys.stdin = open("input4.txt", "r")

def combination(N):
    index_num = [int(x) for x in range(N)]
    result = [index_num[:]]
    c = [0] * len(index_num)
    i = 0
    while i < len(index_num):
        if c[i] < i:
            if i % 2 == 0:
                index_num[0], index_num[i] = index_num[i], index_num[0]
            else:
                index_num[c[i]], index_num[i] = index_num[i], index_num[c[i]]
            result.append(index_num[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

for tc in range(1, int(input())+1):
    N = int(input())
    array = [[int(x) for x in input().split()] for _ in range(N)]
    index_list = combination(N)
    print(index_list)
    res = []
    for i in range(len(index_list)):
        temp = []
        for j in range(N):
            temp.append(array[j][index_list[i][j]])
        res.append(sum(temp))
    print('#{} {}'.format(tc, min(res)))
