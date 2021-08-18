class LNode:
    def __init__(self):
        self.data = None
        self.next = None


def add(h1, h2):
    if h1 is None or h1.next is None:
        return h2

    if h2 is None or h2.next is None:
        return h1

    c = 0  # 判断是否有进位
    sums = 0  # 两链表对应结点相加的和
    # p1和p2为遍历链表的指针
    p1 = h1.next
    p2 = h2.next
    temp_result = None
    result_head = LNode()
    p = result_head  # 指针p指向结果链表的最后一个结点

    while p1 is not None and p2 is not None:
        temp_result = LNode()
        temp_result.next = None
        sums = p1.data + p2.data + c
        temp_result.data = sums % 10
        # c = sums // 10 均可表示向下取整。
        c = int(sums / 10)
        p.next = temp_result
        p = temp_result
        p1 = p1.next
        p2 = p2.next

    if p1 is None:
        while p2 is not None:
            temp_result = LNode()
            temp_result.next = None
            sums = p2.data + c
            temp_result.data = sums % 10
            c = int(sums / 10)
            p.next = temp_result
            p = temp_result
            p2 = p2.next

    if p2 is None:
        while p1 is not None:
            temp_result = LNode()
            temp_result.next = None
            sums = p1.data + c
            temp_result.data = sums % 10
            c = int(sums / 10)
            p.next = temp_result
            p = temp_result
            p1 = p1.next

    if c == 1:
        temp_result = LNode()
        temp_result.next = None
        temp_result.data = 1
        p.next = temp_result

    return result_head


if __name__ == '__main__':
    i = 1
    head1 = LNode()
    head2 = LNode()
    tmp = None
    cur = head1
    addResult = None
    while i < 7:
        tmp = LNode()
        tmp.data = i +2
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    i = 9
    cur = head2
    while i > 4:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i -= 1

    print("head1:", end='')
    cur = head1.next
    while cur is not None:
        print(cur.data, end='')
        cur = cur.next

    print('')

    print("head2:", end='')
    cur = head2.next
    while cur is not None:
        print(cur.data, end='')
        cur = cur.next

    addResult = add(head1, head2)
    print('')

    print("相加后的结果:", end='')
    cur = addResult.next
    while cur is not None:
        print(cur.data, end='')
        cur = cur.next
