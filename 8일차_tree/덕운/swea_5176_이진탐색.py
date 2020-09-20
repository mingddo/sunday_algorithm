import sys

#sys.stdin = open("input.txt", "r")

# 중위 순회 방식으로 숫자가 1부터 채워짐.

def inOrder(index):
    global number
    if index < N+1:
        inOrder(index * 2)
        tree[index] = number
        number += 1
        inOrder(index * 2 + 1)

for test_case in range(1, int(input()) + 1):
    N = int(input())
    tree = [0]*(N+1)
    number = 1
    inOrder(1)
    print('#{} {} {}'.format(test_case, tree[1], tree[N//2]))
