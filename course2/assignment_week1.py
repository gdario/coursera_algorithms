from collections import defaultdict, deque


class Graph:
    def __init__(self, filename):
        self.data = self.read_data(filename)
        self.nodes = {x for line in self.data for x in line}
        self.direct_graph = self.build_direct_graph()
        self.reversed_graph = self.build_reversed_graph()

    @staticmethod
    def read_data(filename):
        with open(filename, 'r', encoding='utf8') as f:
            data = f.read().splitlines()
        data = [[int(x) for x in line.split()] for line in data]
        return data

    def build_direct_graph(self):
        d = defaultdict(list)
        [d[x[0]].append(x[1]) for x in self.data]
        return d

    def build_reversed_graph(self):
        d = defaultdict(list)
        [d[x[1]].append(x[0]) for x in self.data]
        return d

    def dfs_topo(self, graph, start):
        """Run DFS with a given starting node."""
        stack = deque()
        stack.append(start)
        while stack:
            next_node = stack.pop()
            if not self.explored[next_node]:
                self.explored[next_node] = True
                for edge in graph[next_node]:
                    stack.append(edge)
        self.topological_order[start] = self.cur_label
        self.cur_label -= 1

    def toposort(self, graph):
        """Run topological sort of a directed graph."""
        self.explored = {k: False for k in self.nodes}
        self.topological_order = {k: 0 for k in self.nodes}
        self.cur_label = len(self.nodes)
        for v in self.nodes:
            if not self.explored[v]:
                self.dfs_topo(graph, v)

    def kosaraju(self):
        self.toposort(self.reversed_graph)


if __name__ == '__main__':
    graph = Graph('scc.txt')
    graph.kosaraju()
