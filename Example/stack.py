class Stack:

    def __init__(self):
        self.stack = []

    def add(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def peek(self):
        return self.stack[0]

    def remove(self):
        if len(self.stack) <= 0:
            return "No element in the Stack"
        else:
            return self.stack.pop()


stack = Stack()
stack.add(1)
stack.add(2)
stack.peek()
print(stack.peek())
stack.add(3)
stack.add(4)
print(stack.peek())
