# 이건 기존 괄호
def check(sentence):
    stack = []
    for s in sentence:
        if s == '(' or s == '{' or s == '[':
            stack.append(s)
        if s == ')' or s == '}' or s == ']':
            if len(stack) == 0:
                stack.append(s)
                return False  # 조건 1
            else:
                tmp = stack.pop()

                if tmp == '(' and s == ')':
                    continue
                if tmp == '{' and s == '}':
                    continue
                if tmp == '[' and s == ']':
                    continue
                return False  # 조건 2

    if len(stack) > 0:
        return False  # 조건 3

    return True

T = int(input(()))
for test_case in range(1, T+1):
    sentence = list(input())
    print('#{} {}'.format(test_case, check(sentence)))
    # 예외 - ))}{(( 처리중입니다 ㅠㅠ