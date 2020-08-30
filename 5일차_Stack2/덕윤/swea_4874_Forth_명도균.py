import sys

#sys.stdin = open("input.txt", "r")
for test_case in range(1, int(input()) + 1):
    code = list(input().split())
    nums = []
    p = 0
    for c in code:
        if c == '.':
            if not len(nums) == 1:
                p = -1
                # result = 'error'
            else:
                p = 1
                # result = nums.pop()
                break
        try:
            nums.append(int(c))

        except :
            if len(nums) < 2:
                p = -1
                # result = 'error'
                break
            else:
                b = nums.pop()
                a = nums.pop()
                if c == '+':
                    nums.append(a+b)
                elif c == '-':
                    nums.append(a - b)
                elif c == '*':
                    nums.append(a * b)
                elif c == '/':
                    nums.append(a // b)
                    #나눗셈의 경우 float형으로 반환되니깐 무조건 //로 해야해
    if p == -1 or len(nums) != 1:
        print('#{} error'.format(test_case))
    elif p == 1:
        print('#{} {}'.format(test_case , nums[0]))