for t in range(1, int(input())+1):
    aa = int(input())
    a = aa//10
    result = [0, 1, 3]
    for i in range(3, a+1):
        re = result[i-2]*2 + result[i-1]
        result.append(re)
    print('#{} {}'.format(t, result[-1]))