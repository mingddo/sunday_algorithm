import sys
sys.stdin = open("문제1.txt", "r")

# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = [[False]*(N+1) for _ in range(N+1)]
#     for _ in range(M):
#         st_x, st_y, ed_x, ed_y = map(int, input().split())
#         for i in range(st_x, ed_x+1):
#             for j in range(st_y, ed_y+1):
#                 arr[i][j] = True
#
#     result = 0
#     for i in range(N+1):
#         for j in range(N+1):
#             if arr[i][j]:
#                 result += 1
#     print('#{} {}'.format(tc, result))

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        st_x, st_y, ed_x, ed_y = map(int, input().split())
        for i in range(st_x, ed_x+1):
            for j in range(st_y, ed_y+1):
                arr[i][j] += 1
    result = 0
    res = 0
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j]:
                result += 1
                if arr[i][j] > 1:
                    res += 1

    print('#{} {} 겹처진칸 : {}'.format(tc, result, res))