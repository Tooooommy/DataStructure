from collections import deque

q = deque([1, 2, 3, 4])
q.append(5)
print(q)
q.remove(2)
print(q)
q.appendleft(4)
print(q)