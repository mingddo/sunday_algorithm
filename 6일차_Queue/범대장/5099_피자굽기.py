for t in range(1, 1+int(input())):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    duk = [0] * N
    duk_n = [0] * N
    cnt, result = 0, 0
    while True:
        for i in range(N):
            if len(pizzas) == 0:
                if sum(duk) == duk[i]:
                    result = duk_n[duk.index(duk[i])]
                    break
            duk[i] //= 2
            if len(pizzas) > 0 and duk[i] == 0:
                piz = pizzas.pop(0)
                duk[i] = piz
                cnt += 1
                duk_n[i] = cnt
        if result:
            break
    print('#{} {}'.format(t, result))