# def partition(a, begin, end):
#     pivot = (begin + end) // 2
#     L = begin
#     R = end
#     while L < R:
#         while a[L] < a[pivot] and L < R:
#             L += 1
#         while a[R] >= a[pivot] and L < R:
#             R -= 1
#         if L < R:
#             if L == pivot:
#                 pivot = R
#             a[L], a[R] = a[R], a[L]
#         a[pivot], a[R] = a[R], a[pivot]
#         return R
#
# arr = list(map(int, input().split()))
# print(arr)
# s = arr[1]
# e = arr[-1]
# print(partition(arr, s, e))
