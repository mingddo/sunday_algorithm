def dfs(word):
    l = len(word)
    for i in range(l-1):
        if word[i] == word[i + 1]:
            word.pop(i + 1)
            word.pop(i)
            return dfs(word)
    return l


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    words = list(input())
    result = dfs(words)

    print('#{} {}'.format(test_case, result))
            

            
