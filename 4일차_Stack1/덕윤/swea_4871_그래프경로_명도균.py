def dfs(v):
    global result
    visited[v] = 1
    for r in route:
        if r[v] != 0 and visited[r[v]] ==0 :
            if r[v] == end:
                result = 1
            dfs(r[v])

for test_case in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    route = [[0] * (V+1) for _ in range(V+1)]
    for e in range(E):
        a, b = map(int, input().split())
        for p in route:
            if p[a] == 0:
                p[a] = b
                break
    start, end = map(int, input().split())
    result = 0
    visited = [0] * 100
    dfs(start)
    print('#{} {}'.format(test_case, result))

