import sys
sys.stdin = open("input.txt", "r")

def heap_push(n):
    global heap_cnt
    heap_cnt += 1
    heap[heap_cnt] = n
    child = heap_cnt
    parent = child // 2
    while parent and heap[parent] >= heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2

def result():
    n = N // 2
    nn = 0
    while n:
        nn += heap[n]
        n //= 2
    return nn

for t in range(1, 1+int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    heap = [0] * (N+1)
    heap_cnt = 0
    for i in range(N):
        heap_push(nums[i])
    last = result()
    print('#{} {}'.format(t, last))