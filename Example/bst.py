"""
BST将其所有子树分成两部分; 左边的子树和右边的子树，可以定义为 -

left_subtree (keys)  ≤  node (key)  ≤  right_subtree (keys)

"""


class BST(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if self.data > data:  # 左
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = BST(data)
            elif self.data < data:  # 右
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = BST(data)
        else:
            self.data = data

    def find(self, data):
        if self.data > data:  # 左
            if self.left:
                return self.left.find(data)
            return '{} Not Found'.format(data)
        elif self.data < data:  # 右
            if self.right:
                return self.right.find(data)
            return '{} Not Found'.format(data)
        else:
            print('{} is found'.format(self.data))

    def list(self):
        if self.left:
            self.left.list()
        if self.data:
            print(self.data)
        if self.right:
            self.right.list()

    def in_order_traversal(self, root):
        # Left -> Root -> Right
        res = []
        if root:
            res = self.in_order_traversal(root.left)
            res.append(root.data)
            res = res + self.in_order_traversal(root.right)
        return res

    def pre_order_traversal(self, root):
        # Root -> Left ->Right
        res = []
        if root:
            res.append(root.data)
            res = res + self.pre_order_traversal(root.left)
            res = res + self.pre_order_traversal(root.right)
        return res

    def post_order_traversal(self, root):
        # Left ->Right -> Root
        res = []
        if root:
            res = self.post_order_traversal(root.left)
            res = res + self.post_order_traversal(root.right)
            res.append(root.data)
        return res


root = BST(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.find(7))
print(root.find(14))
# root.list()

print(root.in_order_traversal(root))
print(root.pre_order_traversal(root))
print(root.post_order_traversal(root))
