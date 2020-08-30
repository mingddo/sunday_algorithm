for t in range(1,1+int(input())):
    arr = input()
    push = ['{','[','(']
    pull = ['}',']',')']
    li = []
    result = 1
    for i in arr:
        if i in push:
            li.append(i)
        elif (i in pull) and (not li):
            result -= 1
            break
        elif (i in pull) and push.index(li[-1]) != pull.index(i):
            result -= 1
            break
        elif (i in pull) and (push.index(li[-1]) == pull.index(i)):
            li.pop()
    if li:
        result -= 1
    if result < 1:
        print('#{} 0'.format(t))
    else:
        print('#{} 1'.format(t))