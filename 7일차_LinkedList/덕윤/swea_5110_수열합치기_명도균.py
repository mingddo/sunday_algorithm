# import sys
#
# sys.stdin = open("input(1).txt", "r")
#
# for tc in range(1, int(input()) + 1):
#     N, M = map(int,input().split())
#     arr = list(map(int,input().split()))
#
#     for _ in range(M-1):
#         new_list = list(map(int,input().split()))
#         new_a = new_list[0]
#         for i in range(len(arr)):
#             if arr[i] > new_a:
#                 arr = arr[:i]+new_list+arr[i:]
#                 break
#         else:
#             arr = arr + new_list
#
#     print('#{}'.format(tc),end=' ')
#     for _ in range(10):
#         print(arr.pop(),end=' ')
#     print()
import sys
sys.stdin = open('5110.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))

    for _ in range(M-1):
        new_list = list(map(int,input().split()))
        new_a = new_list[0]
        for i in range(len(arr)):
            if arr[i] > new_a:
                arr[i:i]= new_list
                break
        else:
            arr = arr + new_list

    print('#{}'.format(tc), end=' ')
    for _ in range(10):
        print(arr.pop(), end=' ')
    print()