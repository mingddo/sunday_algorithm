def pattern(str1, str2):
    a = len(str1)
    b = len(str2)
    # 초기값
    i = a-1
    j = a-1
    cnt = 0
    result = 0
    while True:
        if (j >= b) or (i >= a):
            break
        # 끝자리부터 비교
        if (str1[i] == str2[j]) and (i != 0):
            i -=1
            j -=1
            if i == 0:
                result = 1
                break
        # 같지 않다면, str1에 str1[j]가 있는지
        else:
            for s in str1[::-1]:
                cnt += 1
                if s == str2[j]:
                    i = a-1
                    j += cnt - 1
                    cnt = 0
                    break
            if cnt == a:
                i = a-1
                j += a
                cnt = 0
        if i == 0:
            break
    return result

T=int(input())
for test_case in range(1,T+1):
    str1 = list(input())  # 길이 N
    str2 = list(input())  # 길이 M
    print('#{} {}'.format(test_case, pattern(str1, str2)))