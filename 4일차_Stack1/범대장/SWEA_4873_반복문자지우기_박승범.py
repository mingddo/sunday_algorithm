import sys
sys.stdin = open("input.txt", "r")

for t in range(1,1+int(input())):
    strings = input()
    new_s = []
    for i in strings:
        if not new_s:
            new_s.append(i)
        elif new_s[-1] != i:
            new_s.append(i)
        else:
            new_s.pop()
    print('#{} {}'.format(t, len(new_s)))