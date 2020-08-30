import sys
sys.stdin = open("input.txt", "r")

def DFS(s):
    visited[s] = 1
    for i in range(1, V+1):
        if arr[s][i] == 1 and visited[i] == 0:
            DFS(i)

for t in range(1, 1+int(input())):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        st, en = map(int, input().split())
        arr[st][en] = 1
    S, G = map(int, input().split())
    DFS(S)
    if visited[G] == 1:
        print('#{} 1'.format(t))
    else:
        print('#{} 0'.format(t))