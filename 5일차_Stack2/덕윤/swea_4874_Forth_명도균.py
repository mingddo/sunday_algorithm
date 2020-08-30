import sys

#sys.stdin = open("input.txt", "r")
for test_case in range(1, int(input()) + 1):
    code = list(input().split())
    nums = []
    result = 'error'
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

        except ValueError :
            if len(nums) < 2:
                p = -1
                # result = 'error'
                break
            else:
                b = nums.pop()
                a = nums.pop()
                if c == '+':
                    nums.append((a+b))
                elif c == '-':
                    nums.append((a - b))
                elif c == '*':
                    nums.append((a * b))
                elif c == '/':
                    nums.append((a / b))
    if p == -1 or len(nums) != 1:
        print('#{} error'.format(test_case))
    elif p == 1:
        print('#{} {}'.format(test_case , nums[0]))