import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N, M, L =  map(int, input().split())
    tree = [0] * (N+1)
    visited = []
    node = list(range(N, 1, -1))
    for _ in range(M):
        a, b = map(int,input().split())
        tree[a] = b
        visited.append(a)
    for n in node:
        tree[n//2] += tree[n]
    print('#{} {}'.format(test_case,tree[L]))
