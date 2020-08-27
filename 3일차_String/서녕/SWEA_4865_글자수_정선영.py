def count(str1, str2):
    cnt = [0] * len(str1)
    for i in range(len(str1)):
        for t in str2:
            if str1[i] == t:
                cnt[i] += 1
    return max(cnt)

T = int(input())
for test_case in range(1,T+1):
    str1 = list(input()) # 길이 N
    str2 = list(input())  # 길이 M (>=N)
    print('#{} {}'.format(test_case, count(str1, str2)))
