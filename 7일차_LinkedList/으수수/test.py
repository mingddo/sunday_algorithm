class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


def addList(lst, arr):
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new

    if lst.head is None:
        lst.head, lst.tail = first, last
    else:
        cur = lst.head
        while cur is not None:
            if cur.data > arr[0]: break
            cur = cur.next
        if cur is None:  # 뒤에 # 순서주의
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last
        elif cur.prev is None:  # 앞에
            last.next = lst.head
            lst.head.prev = last
            lst.head = first
        else:  # 중간에 추가
            prev = cur.prev
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
    lst.size += len(arr)


def printList(lst):  # 연결리스트 출력
    if lst.head is None:
        return
    cur = lst.tail
    cnt = 10
    while cnt:  # 역방향
        print(cur.data, end=' ')
        cur = cur.prev
        cnt -= 1
    print()


import sys
sys.stdin = open('5110.txt', 'r')

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(m))  # 2차원배열로 받기
    mylist = LinkedList()
    for i in range(m):
        addList(mylist, arr[i])
    print(f'#{tc}', end=' ')
    printList(mylist)
