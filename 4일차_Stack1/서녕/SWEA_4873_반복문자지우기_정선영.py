def erase(sentence):
    i = 0
    tmp = []
    while True:
        if i == len(sentence) -1:
            break
        if sentence[i] == sentence[i+1]:
            del sentence[i:i+2]
            i = 0
        else:
            i += 1
    return len(sentence)

T = int(input())
for test_case in range(1, T+1):
    sentence = list(input())
    print('#{} {}'.format(test_case, erase(sentence)))
