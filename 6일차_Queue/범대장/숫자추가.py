import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 1+int(input())):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    for _ in range(M):
        l, n = map(int, input().split())
        nums.insert(l, n)
    print('#{} {}'.format(t, nums[L]))