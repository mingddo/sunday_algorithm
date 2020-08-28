def route(start):
    global result
    visited[start] = 1 # 현재 노드
    for next in range(1, V+1):
        if graph[start][next] == 1 and (not visited[next]):
            if next == G:
                result = 1
                return
            route(next)

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())  # V개 노드, E개 경로
    graph = [[0] * (V+1) for _ in range(V+1)]  # 0부터 VbyV
    visited = [0] * (V+1)
    for i in range(E):
        start, end = map(int, input().split())  # E개의 간선 정보
        graph[start][end] = 1  # 방향 있음

    S, G = map(int, input().split())  # 출발노드 S, 도착노드 G
    result = 0  # 경로 있으면 1, 없으면 0
    route(S)
    print('#{} {}'.format(test_case, result))
