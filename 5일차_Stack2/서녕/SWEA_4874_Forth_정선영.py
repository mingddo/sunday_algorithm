T = int(input())
for test_case in range(1, T+1):
    example = list(input().split())
    stack = []
    flag = 0
    # Forth(example)
    for ex in example:
        if ex == '.':
            break
        if ex.isdigit():
            stack.append(int(ex))
        else:
            try:
                x2, x1 = stack.pop(), stack.pop()
                if ex == '+':
                    result = x1 + x2
                elif ex == '-':
                    result = x1 - x2
                elif ex == '*':
                    result = x1 * x2
                elif ex == '/':
                    result = x1 // x2
                stack.append(result)
            except:
                flag = 'error'

    if flag == 0 and len(stack) == 1:
        print('#{} {}'.format(test_case, stack[0]))
    elif flag == 'error' or len(stack) > 1:
        print('#{} error'.format(test_case))

