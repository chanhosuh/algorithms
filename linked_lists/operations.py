

def delete(head, data):
    ''' removes first node with given data '''
    if not head:
        return head

    if head.data == data:
        return head.next
    else:
        prev = head
        curr = head.next
        while curr and curr.data != data:
            prev = curr
            curr = curr.next

        if curr:
            prev.next = curr.next

        return head


def remove_duplicates(head):
    vals = set()

    if not (head and head.next):
        # 0 or 1 nodes in list
        return head

    vals.add(head.data)

    # start iterating on 2nd node
    prev = head
    curr = head.next
    while curr:
        if curr.data in vals:
            # delete node
            # case 1: when next node exists, set curr to next node
            if curr.next:
                curr.data = curr.next.data
                curr.next = curr.next.next
            # case 2: when curr node is last
            else:
                prev.next = None
                curr = None
        else:
            vals.add(curr.data)
            prev = curr
            curr = curr.next

    return head

