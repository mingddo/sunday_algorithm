def arr_sum(sum, r):
    global minValue
    if sum >= minValue:
        return
    if r == N:
        minValue = min(sum, minValue)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            arr_sum(sum + arr[r][i], r+1)
            visited[i] = 0

# test_case
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    minValue = 987654321

    arr_sum(0, 0)
    print('#{} {}'.format(test_case, minValue))