import sys
sys.stdin = open("input.txt", "r")

def InOder(index):
    global cnt
    if tree[index * 2] != 0:
        InOder(index*2)
    tree[index] = cnt
    cnt += 1
    if tree[index * 2 + 1] != 0:
        InOder(index * 2 + 1)
for t in range(1, 1+int(input())):
    N = int(input())
    tree = [-1]*(N+1) +[0] * (N+1)
    cnt = 1
    InOder(1)
    print('#{} {} {}'.format(t, tree[1], tree[N//2]))