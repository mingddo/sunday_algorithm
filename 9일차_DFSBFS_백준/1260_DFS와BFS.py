import sys
sys.stdin = open("input.txt", "r")
def DFS(s):
    global resultDFS
    resultDFS += str(s)
    visitedDFS[s] = 1
    for i in range(1, N+1):
        if arr[s][i] == 1 and visitedDFS[i] == 0:
            DFS(i)

def BFS(s):
    global resultBFS
    q = []
    q.append(s)
    visitedBFS[s] = 1
    resultBFS += str(s)
    while q:
        qq = q.pop(0)
        for i in range(1, N+1):
            if arr[qq][i] == 1 and visitedBFS[i] == 0:
                resultBFS += str(i)
                visitedBFS[i] = 1
                q.append(i)
# main
N, M, V = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for m in range(M):
    r, c = map(int, input().split())
    arr[r][c] = arr[c][r] = 1
# DFS
visitedDFS = [0]*(N+1)
resultDFS = ''
DFS(V)
# BFS
visitedBFS = [0]*(N+1)
resultBFS = ''
BFS(V)
for i in resultDFS:
    print(i, end=' ')
print()
for i in resultBFS:
    print(i, end=' ')
print()
