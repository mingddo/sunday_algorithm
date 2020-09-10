def BFS(s):
    q = []
    q.append(s)
    visited[s] = 1
    while len(q):
        r = q.pop(0)
        for j in range(1, V+1):
            if arr[r][j] == 1 and visited[j] == False:
                if j == G:
                    return visited[r]
                else:
                    q.append(j)
                    visited[j] = visited[r] + 1
    return 0

for t in range(1, 1+int(input())):
    V, E = map(int, input().split())
    arr = [[False]*(V+1) for _ in range(V+1)]
    visited = [False]*(V+1)
    for i in range(E):
        a, b = map(int, input().split())
        arr[a][b] = arr[b][a] = 1
    S, G = map(int, input().split())
    result = BFS(S)
    print('#{} {}'.format(t, result))