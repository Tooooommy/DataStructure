class Queue:

    def __init__(self):
        self.queue = list()

    def add(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False

    def size(self):
        return len(self.queue)

    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return "No elements in Queue!"


queue = Queue()
queue.add(1)
queue.add(2)
queue.add(3)
print(queue.size())
print(queue.remove())