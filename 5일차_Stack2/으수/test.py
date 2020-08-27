def sol(x):
    cnt=0
    for y in range(1,100):
        cnt+=1
        if x and arr[y][x-1]:
            while x and arr[y][x-1]:
                x-=1
                cnt+=1
        elif x<99 and arr[y][x+1]:
            while x<99 and arr[y][x+1]:
                x+=1
                cnt+=1
    return cnt
for t in range(10):
    input()
    arr=[list(map(int,input().split()))for _ in range(100)]
    tmp=100000
    ans=0
    for j in range(100):
        if arr[0][j]:
            if tmp>sol(j):
                tmp=sol(j)
                ans=j
    print('#{} {}'.format(t+1,ans))