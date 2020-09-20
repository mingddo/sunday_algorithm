import sys

#sys.stdin = open("input.txt", "r")
def f(start):
    global tree
    cnt = 0
    q= [start]
    while q:
        v = q.pop(0)
        cnt += 1
        for t in tree:
            if t[v] != 0:
                q.append(t[v])
    return cnt


for test_case in range(1, int(input()) + 1):
    E, N = map(int, input().split())
    tree = [[0]*(E+2) for _ in range(2)]
    arr = list(map(int,input().split()))
    for i in range(len(arr)//2):
        a, b = arr[2*i], arr[2*i+1]
        if not tree[0][a]:
            tree[0][a] = b
        else:
            tree[1][a] = b
    result = f(N)
    print('#{} {}'.format(test_case,result))