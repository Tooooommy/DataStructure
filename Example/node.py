"""
节点
"""


class node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


n1 = node(1)
n2 = node(2)
n3 = node(3)
n4 = node(4)

n1.next = n2
n2.next = n3
n3.next = n4

element = n1

while element:
    print(element.data)
    element = element.next
