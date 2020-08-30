import sys


# sys.stdin = open("input.txt", "r")
# 가위 바위보 함수
# 두명이면 게임하고,
# 한 명이면 게임하지 않고 pass (stack에 저장)
def game(p1, p2):
    num_1, car_1 = p1
    num_2, car_2 = p2
    win = (num_1, car_1)
    if car_1 == 1:
        if car_2 == 1:
            if num_1 > num_2:
                win = (num_2, car_2)
        elif car_2 == 2:
            win = (num_2, car_2)
    elif car_1 == 2:
        if car_2 == 2:
            if num_1 > num_2:
                win = (num_2, car_2)
        elif car_2 == 3:
            win = (num_2, car_2)
    else:
        if car_2 == 1:
            win = (num_1, car_1)
        elif car_2 == 2:
            win = (num_2, car_2)
        else:
            if num_1 > num_2:
                win = (num_2, car_2)
    return win
# 그룹 2는 무조건 짝수개
def pair(n, group):
    new_group = []
    for i in range(n):
        new_group.append(game(group[2*i],group[2*i+1]))
    return new_group

for test_case in range(1, int(input()) + 1):
    N = int(input())
    li = list(map(int, input().split()))
    e_list = list(enumerate(li))
    g_1 = e_list[:N//2]
    g_2 = e_list[N//2:]
    while True:
        if len(g_1) == 1:
            break
        g_1 = pair(len(g_1)-1, g_1)

    while True:
        if len(g_2) == 1:
            break
        g_2 = pair(len(g_2)-1, g_2)
    z, r = game(g_1[0],g_2[0])
    print(z+1)