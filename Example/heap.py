"""
堆是一种特殊的树结构
其中每个父节点小于或等于其子节点。 然后它被称为最小堆(Min Heap)
如果每个父节点大于或等于其子节点，则称它为最大堆(Max Heap)
"""
import heapq

H = [21,1,45,78,3,5]
heapq.heapify(H)
print(H)
heapq.heappush(H,8)
print(H)
heapq.heappop(H)
print(H)
heapq.heapreplace(H,6)
print(H)
