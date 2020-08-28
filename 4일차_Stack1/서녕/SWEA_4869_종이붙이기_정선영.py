# memoization 활용
def find(N):
    # 0으로 index 순서 맞추기
    # find(1) = 길이 10 *1 (1가지)
    # find(3) = 길이 10 *2 (2가지) + 길이 20 *1 (1가지)
    memory = [0, 1, 3]
    n = N // 10  # index
    for i in range(3, N+1):
        x = memory[i-1] + memory[i-2] * 2
        memory.append(x)
    return memory[n]

for test_case in range(1, int(input()) + 1):
    N = int(input())
    print('#{} {}'.format(test_case, find(N)))