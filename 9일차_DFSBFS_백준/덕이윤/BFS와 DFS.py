def dfs(v):
    b_visited[v] = 1
    print(v, end=' ')
    for x in sorted(arr[v]):
        if not b_visited[x]:
            dfs(x)

def bfs(s):
    q = [s]
    visited = [s]
    while q:
        f = q.pop(0)
        print(f, end=' ')
        for y in sorted(arr[f]):
            if y not in visited:
                q.append(y)
                visited.append(y)



N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]
for m in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
dx = [1,-1,0,0]
dy = [0,0, 1,-1]
b_visited = [0] * (N+1)
dfs(V)
print()
bfs(V)
print()