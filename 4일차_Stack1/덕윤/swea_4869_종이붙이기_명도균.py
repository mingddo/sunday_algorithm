
def box(a):
    if a == 1:
        return 1
    if a == 2:
        return 3
    return box(a-1) + (2 * box(a-2))
for test_case in range(1, int(input()) + 1):
    N = int(input())
    result = box(N//10)
    print('#{} {}'.format(test_case, result))

# n의 수는 n-1 과 n-2의 합.
# n-1의 경우 n-1 + 10짜리 -1가지
# n-2의 경우 n-2와 20짜리 (20을 10 가로로 채운 것도 있으니) * 2 -2가지