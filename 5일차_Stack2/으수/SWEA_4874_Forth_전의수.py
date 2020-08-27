import sys
sys.stdin = open("input1.txt", "r")

def calculate():
    n1 = stack.pop()
    n2 = stack.pop()
    if temp[i] == "+":
        result = n1 + n2
    elif temp[i] == "-":
        result = n1 - n2
    elif temp[i] == "*":
        result = n1 * n2
    elif temp[i] == "/":
        result = n1 // n2
    stack.append(result)


for tc in range(1, int(input())+1):
    temp = list(input().split())
    stack = []
    error = False
    for i in range(len(temp)-1):
        if temp[i].isdigit():
            stack.append(int(temp[i]))
        else:
            try:
                calculate()
            except:
                error = True
    if error == False and len(stack) == 1:
        res = stack[0]
    elif error == True or len(stack) > 1:
        res = 'error'
    print('#{} {}'.format(tc, res))