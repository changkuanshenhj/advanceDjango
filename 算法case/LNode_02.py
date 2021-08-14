class LNode:
    def __init__(self):
        self.data = None
        self.next = None


def removedup1(head):
    if head is None or head.next is None:
        return
    outerCur = head.next
    innerCur = None
    innerPre = None

    while outerCur is not None:
        innerCur = outerCur.next
        innerPre = outerCur
        while innerCur is not None:
            if outerCur.data == innerCur.data:
                innerPre.next = innerCur.next
                innerCur = innerCur.next
            else:
                innerPre = innerCur
                innerCur = innerCur.next

        outerCur = outerCur.next


def removeduprecursion(head):
    if head.next is None:
        return head
    pointer = None
    cur = head
    head.next = removeduprecursion(head.next)
    pointer = head.next
    while pointer is not None:
        if head.data == pointer.data:
            cur.next = pointer.next
            pointer = pointer.next
        else:
            cur = pointer
            pointer = pointer.next

    return head


def removedup2(head):
    if head is None:
        return
    head.next = removeduprecursion(head.next)


if __name__ == '__main__':
    i = 1
    head = LNode()
    head.next = None
    tmp = None
    cur = head
    while i < 7:
        tmp = LNode()
        if i % 2 == 0:
            tmp.data = i + 1
        elif i % 3 == 0:
            tmp.data = i - 2
        else:
            tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    print("删除重复结点前:", end='')
    cur = head.next
    while cur is not None:
        print(cur.data, end='')
        cur = cur.next

    # removedup1(head)
    removedup2(head)
    print("删除重复结点后:", end='')
    cur = head.next
    while cur is not None:
        print(cur.data, end='')
        cur = cur.next