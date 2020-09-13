def solution(info, query):
    answer = []
    arr = []
    Q = []
    for i in info:
        arr.append(list(i.split()))
    for j in range(len(query)):
        Q.append(list(query[j].split()))
        #and를 제거하는 작업
        Q[j].pop(5)
        Q[j].pop(3)
        Q[j].pop(1)
    #### 여기까지 비교를 위한 리스트 배열 저장함.
    for x in range(len(Q)):
        search = list(range(len(arr)))
        sub_search =[]
        k = 0
        while k < 5:
            if k == 4:
                for y in search:
                    if int(arr[y][k]) >= int(Q[x][k]):
                        sub_search.append(y)
                answer.append(len(sub_search))
                k += 1
            else:
                if Q[x][k] != '-':
                    for y in search:
                        if arr[y][k] == Q[x][k]:
                            sub_search.append(y)
                    search = sub_search
                    sub_search = []
                    k += 1
                else:
                    k += 1
    return answer

# k = solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])
# print(k)