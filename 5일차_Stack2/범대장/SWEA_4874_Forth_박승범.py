import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 1+int(input())):
    forth = list(input().split())
    new_forth = []
    resultex = 0
    for i in range(len(forth)-1):
        if forth[i].isdigit():
            new_forth.append(int(forth[i]))
        else:
            try:
                b, a = new_forth.pop(), new_forth.pop()
                if forth[i] == '+':
                    c = a + b
                elif forth[i] == '-':
                    c = a - b
                elif forth[i] == '*':
                    c = a * b
                elif forth[i] == '/':
                    c = a // b
                new_forth.append(c)
            except:
                new_forth.insert(0, 'error')
    if len(new_forth) > 1:
        result = 'error'
    else:
        result = new_forth[0]
    print('#{} {}'.format(t, result))
