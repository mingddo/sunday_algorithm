for test_case in range(1, int(input()) + 1):
    str_list = list(input())
    n = len(str_list)
    left = ['(', '{']
    right = [')', '}']
    result = 1
    stack = []
    for s in str_list:
        if s in left:
            stack.append(s)
        elif s in right:
            if len(stack) == 0:
                result = 0
                break
            elif right.index(s) != left.index(stack[-1]):
                result = 0
                break
            else:
                stack.pop()
    if len(stack) != 0:
        result = 0

    print('#{} {}'.format(test_case, result))
