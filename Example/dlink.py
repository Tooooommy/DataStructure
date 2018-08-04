class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLink(object):
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def list(self, node):
        while node:
            print(node.data)
            node = node.next

    def insert(self, prev_node, new_data):
        if prev_node is None:
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not Node:
            new_node.next.prev = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = new_node
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last


dllist = DoubleLink()
dllist.push(12)
dllist.push(8)
dllist.push(62)
dllist.insert(dllist.head.next, 13)
dllist.append(45)
dllist.list(dllist.head)
