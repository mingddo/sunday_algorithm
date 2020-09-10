for t in range(1, 1+int(input())):
    N, M = map(int, input().split())
    nums = input().split()
    print('#{} {}'.format(t, nums[M%N]))