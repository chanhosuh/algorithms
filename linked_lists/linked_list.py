


class Node(object):

    def __init__(self, data, next):
        self.data = data
        self.next = next


def delete(head, data):
    ''' removes first node with given data '''
    if head:
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
    else:
        return head


class LinkedList(object):

    def __init__(self, data_list=None):
        self.head = None
        if data_list:
            for data in data_list:
                self.push(data)

    def push(self, data):
        self.head = Node(data, self.head)

    def pop(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data
        else:
            return None

    def append(self, data):
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data, None)
        else:
            self.head = Node(data, None)

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next


if __name__ == '__main__':
    data_list = [4, 3, 2, 1]
    linked_list = LinkedList(data_list)
    linked_list.pop()
    linked_list.push(1)
    
    
    
# remove duplicates


def remove_duplicates(linked_list):
    head = linked_list.head
    vals = {}
    
    if not head:
        return head
    
    if not head.next:
        return head
    
    prev = head
    vals[head.data] = 1
    
    # start iterating on 2nd node
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
            vals[curr.data] = 1
            prev = curr
            curr = curr.next
        
    linked_list.head = head
    
    
