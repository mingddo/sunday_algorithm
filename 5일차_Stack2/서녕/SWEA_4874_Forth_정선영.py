## 테스트케이스 10개 중 1개 오답..........뭘까

def calculator(str1, a, b):  # 여기서 a, b는 str_num
    if str1 == '+':
        return int(a)+int(b)
    if str1 == '-':
        return int(a)-int(b)
    if str1 == '*':
        return int(a)*int(b)
    if str1 == '/':
        return int(a)//int(b) # 근데 어차피 항상 나누어 떨어진다

def Forth(lsts):
    cal_type = ['+', '-', '*','/']
    stack = []
    for lst in lsts:
        if lst.isdigit():  # 숫자 '10'
            stack.append(lst)
            continue
        elif lst in cal_type:  # 연산자
            cal =lst
            if len(stack) < 2:
                print('error')
                break
            else:
                x1 = stack.pop()  # 그 다음 들어간 애
                x2 = stack.pop()  # 먼저 들어간 애
                tmp = calculator(cal, x2, x1)
                stack.append(str(tmp))
                continue
        elif lst == '.':
            if len(stack) == 0:
                print('error')
                break
            else:
                print(stack.pop())
                break

T = int(input())
for test_case in range(1, T+1):
    example = list(input().split())
    print('#{} '.format(test_case), end="")
    Forth(example)
