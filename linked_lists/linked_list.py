from collections import namedtuple

Node = namedtuple('Node', 'data next')


class LinkedList(object):

    def __init__(self, data_list=None):
        self.head = None
        if data_list:
            for data in data_list:
                self.push(data)

    def push(self, data):
        """ adds new node with given data to head of list """
        self.head = Node(data, self.head)

    def pop(self):
        """ removes head of list and returns its data """
        if not self.head:
            return None

        data = self.head.data
        self.head = self.head.next
        return data

    def append(self, data):
        """ adds new node with given data to tail of list """
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data, None)
        else:
            self.head = Node(data, None)

    def __iter__(self):
        """ iterates through list of data """
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next

    def __str__(self):
        return ', '.join([str(data) for data in self])


if __name__ == '__main__':
    data_list = [4, 3, 2, 1]
    linked_list = LinkedList(data_list)
    print(linked_list)
    linked_list.pop()
    print(linked_list)
    linked_list.push(1)
    print(linked_list)
