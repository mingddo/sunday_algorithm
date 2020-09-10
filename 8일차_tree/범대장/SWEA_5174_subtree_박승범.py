import sys
sys.stdin = open("input.txt", "r")

def search(p):
    global cnt
    for i in range(2):
        if tree[p][i] == 0:
            return
        elif tree[p][i] != 0:
            cnt += 1
            search(tree[p][i])

for t in range(1, 1+int(input())):
    E, N = map(int, input().split())
    nums = list(map(int, input().split()))
    tree = [[0] * 2 for _ in range(E+2)]
    cnt = 1
    for e in range(0, len(nums), 2):
        parent = nums[e]
        child = nums[e+1]
        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
    search(N)
    print('#{} {}'.format(t, cnt))




