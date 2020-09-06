import sys

sys.stdin = open("input.txt", "r")
def plus(a,b):
    global nums
    c_list = nums[a:]
    plus_l = nums[:a]
    plus_l.append(b)
    nums = plus_l + c_list
    return

for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    nums = list(map(int,input().split()))
    for m in range(M):
        x, y = map(int, input().split())
        plus(x,y)
    print('#{} {}'.format(tc,nums[L]))
