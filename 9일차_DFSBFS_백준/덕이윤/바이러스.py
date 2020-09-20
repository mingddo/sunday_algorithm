def bfs(v):
    visited = [1]
    q = [1]
    while q:
        s = q.pop(0)
        for x in arr[s]:
            if x not in visited:
                q.append(x)
                visited.append(x)
    return (len(visited)-1)

N = int(input())
M = int(input())
arr = [[]for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
print(bfs(1))