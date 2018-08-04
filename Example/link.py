class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Link(object):
    def __init__(self):
        self.head = None

    def list(self):
        head = self.head
        while head:
            print(head.data)
            head = head.next

    def insert(self, new_data, at_num):
        if self.head is None:
            return
        node = Node(new_data)
        if at_num == 0:  # 开头插入node
            node.next, self.head = self.head, node
        else:
            head = self.head
            while at_num - 1 > 0:
                at_num -= 1
                if head.next is None:
                    break
                head = head.next

            node.next = head.next
            head.next = node

    def size(self):
        size = 0
        head = self.head
        while head:
            size += 1
            head = head.next

        return size

    def insert_at_begin(self, new_data):
        self.insert(new_data, 0)

    def insert_at_end(self, new_data):
        self.insert(new_data, self.size())

    @staticmethod
    def insert_at_node(new_data, node):
        if node is None:
            print("node is None")
            return

        new_node = Node(new_data)
        new_node.next = node.next
        node.next = new_node

    def remove(self, at_num):
        size = self.size()
        if self.head is Node or at_num > size or at_num == 0:
            print('link is Node or at_num = 0/ > size')
            return

        head = self.head
        if at_num == 1:
            self.head = self.head.next
        elif at_num == size:
            print(at_num)
            while at_num > 2:
                at_num -= 1
                head = head.next
            head.next = None
        else:
            while at_num > 2:
                at_num -= 1
                head = head.next
            head.next = head.next.next


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

link = Link()
link.head = n1
link.head.next = n2  # // n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
# link.list()
# link.insert(6, 7)
# print(link.size())
# print(link.head.next)
# link.insert_at_node(8, n3)
link.remove(4)
link.list()
