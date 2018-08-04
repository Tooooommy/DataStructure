"""
图是一组对象通过链接连接的一组对象的图形表示。 互连对象由称为顶点的点表示，连接顶点的链接称为边
V = {a, b, c, d, e}             # 点
E = {ab, ac, bd, cd, de}        # 边
"""
import collections

graph = {"a": ["b", "c"],
         "b": ["a", "d"],
         "c": ["a", "d"],
         "d": ["e"],
         "e": ["d"]
         }


# print(graph)


class Graph(object):
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def get_v(self):
        return list(self.gdict.keys())

    def add_v(self, v):
        if v not in self.gdict:
            self.gdict[v] = []

    def get_e(self):
        return self.find_e()

    def add_e(self, e):
        e = set(e)
        v1, v2 = tuple(e)
        if v1 in self.gdict:
            self.gdict[v1].append(v2)
        else:
            self.gdict[v1] = [v2]

    def find_e(self):
        e_name = []
        for v in self.gdict:
            for nx_v in self.gdict[v]:
                if [nx_v, v] not in e_name:
                    e_name.append([v, nx_v])
        return e_name

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start)
        for next in set(self.gdict[start]) - visited:
            self.dfs(next, visited)
        return visited

    def bfs(self, startnode):
        seen, queue = {startnode}, collections.deque([startnode])
        while queue:
            vertex = queue.popleft()
            print(vertex)
            for node in graph[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)


g = Graph(graph)
# print(g.get_v())
# g.add_v('f')
# print(g.get_v())
# g.add_e(['a', 'e'])
# g.add_e(['a', 'c'])
# print(g.get_e())
print(g.dfs('a'))
print(g.bfs('a'))
