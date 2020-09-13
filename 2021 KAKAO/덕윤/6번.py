def up(board, sx,sy,dx,dy):
    if sx == dx:
        return 0
    count = 0
    a = sx
    while a != dx:
        #밑에 있을 때: 커짐
        if a > dx:
            a -= 1
            if board[a][sy]:
                count += 1
        # 아래에 있을 때
        elif a < dx:
            a += 1
            if board[a][sy]:
                count += 1
        #같은 경우는 아예 함수 실행을 안하고 side 함수를 실행시키면됨.
    return count + 1

#양옆으로 움직이는 사이드 함수.
def side(board, sx,sy,dx,dy):
    if sy == dy:
        return 0
    count = 0
    b = sy
    while b != dy:
        if b > dy:
            b -= 1
            if board[sx][b]:
                count += 1
        # 아래에 있을 때
        elif b < dy:
            b += 1
            if board[sx][b]:
                count += 1
    return count + 1
d_x = [-1,1,0,0]
d_y = [0,0,-1,1]
q = []

def findcard(board,p,r):
    count = 0
    q.append((p,r))
    while q:
        x,y =q.pop(0)
        for d in range(4):
            nx = x + d_x[d]
            ny = y + d_y[d]
            if 0 <= nx < 4 and 0<=ny<4 and (nx,ny) not in q:
                if board[nx][ny] != 0:
                    return (nx,ny)
                q.append((nx,ny))

def solution(arr, r, c):
    board = arr
    cnt = 0
    answer = 0
    target = 0
    startx = r
    starty = c
    pairx = -1
    pairy = -1
    card = [0]*7
    for c1 in range(4):
        for c2 in range(4):
            if board[c1][c2] and card[board[c1][c2]] == 0:
                card[board[c1][c2]] = 1
    #여기에 몇 번 반복할 건지 쓰면 됨.
    # 처음 배열에 있는 경우와 없는 경우
    while card.count(0) < 7:
        if board[r][c]:
            cnt += 1 #엔터치는 것
            target = board[r][c]
            #타겟을 찾았으면 나머지 타겟의 좌표가 어디 있는지 찾아야 함.
            for i in range(4):
                if pairx != -1:
                    break
                for j in range(4):
                    if board[i][j] == target and (i,j) != (r,c):
                        pairx = i
                        pairy = j
                        break
            #옆 먼저가는것
            s_f1 = side(board, r, c, pairx, pairy)
            s_f2 = up(board, r, pairy, pairx, pairy)
            # 위 아래 탐색을 먼저 하는 것
            u_f1 = up(board, r, c, pairx, pairy)
            u_f2 = side(board, pairx, c, pairx, pairy)
            # 짝 찾으면 0 으로 초기화 시켜줌
            board[r][c] = board[pairx][pairy] = 0
            if s_f1 + s_f2 < u_f1 + u_f2:
                cnt += s_f1 + s_f2
                r = pairx
                c = pairy
            else:
                cnt += u_f1 + u_f2
                r = pairx
                c = pairy
            card[target] = 0
        else:#r,c에서 가장 가까운 카드 찾기.
            r_r, c_c = findcard(board, r,c)
            s_f1 = side(board, r, c, r_r, c_c)
            s_f2 = up(board, r, c_c, r_r, c_c)
            # 위 아래 탐색을 먼저 하는 것
            u_f1 = up(board, r, c, r_r, c_c)
            u_f2 = side(board, r_r, c, r_r, c_c)
            if s_f1 + s_f2 < u_f1 + u_f2:
                cnt += s_f1 + s_f2
            else:
                cnt += u_f1 + u_f2
            r = r_r
            c = c_c
    answer = cnt

    return answer

k = solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1)
print(k)