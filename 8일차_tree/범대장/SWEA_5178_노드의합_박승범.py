import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 1+int(input())):
    N, M, L = map(int, input().split())
    if N % 2 == 0:
        tree = [1] + [0] * (N+1) # 하나 더
    else:
        tree = [0] * (N+1)
    for m in range(M):
        index, value = map(int, input().split())
        tree[index] = value
    for i in range(tree[0] + N, 1, -2):
        tree[i // 2] = tree[i] + tree[i - 1]
    print('#{} {}'.format(t, tree[L]))