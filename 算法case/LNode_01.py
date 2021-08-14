class LNode:
    def __init__(self):
        self.data = None
        self.next = None


# 就地逆序
def reverse1(head):
    if head is None or head.next is None or head.next.next is None:
        return
    pre = None
    cur = None
    next = None

    cur = head.next
    next = cur.next
    cur.next = None
    pre = cur
    cur = next

    while cur.next is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    cur.next = pre
    head.next = cur


# 插入法
def reverse2(head):
    if head is None \
            or head.next is None:
        return
    cur = None
    next = None
    cur = head.next.next
    head.next.next = None

    while cur is not None:
        next = cur.next
        cur.next = head.next
        head.next = cur
        cur = next


# 递归法
def recursive_reverse(head):
    if head is None or head.next is None:
        return head
    else:
        newhead = recursive_reverse(head.next)
        head.next.next = head
        head.next = None
    return newhead


def reverse3(head):
    if head is None:
        return
    fistNode = head.next
    newhead = recursive_reverse(fistNode)
    head.next = newhead
    return head


# 逆序输出链表的内容
def reverse_print(firstNode):
    if firstNode is None:
        return
    reverse_print(firstNode.next)
    print(firstNode.data)
    return


if __name__ == '__main__':
    i = 1
    head = LNode()
    head.next = None
    tmp = None
    cur = head

    # 构造单链表
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    print("逆序前:", end='')
    cur = head.next
    while cur is not None:
        print(cur.data, end='')
        cur = cur.next
    print('\n逆序后:', end='')
    # reverse2(head)
    head = reverse3(head)
    cur = head.next
    while cur is not None:
        print(cur.data, end='')
        cur = cur.next
