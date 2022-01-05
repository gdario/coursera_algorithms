from collections import deque


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.topo_order = {k: 0 for k in self.graph}
        self.explored = {k: False for k in self.graph}
        self.cur_label = len(self.graph)

    @staticmethod
    def read_graph(filename):
        """Read a graph provided as an adjacency list."""
        adj_dict = {}
        with open(filename, 'r') as f:
            for line in f:
                line = [int(x) for x in line.strip().split()]
                adj_dict[line[0]] = line[1:]
        return adj_dict

    def dfs(self, start):
        """Run DFS with a given starting node."""
        self.explored = {k: False for k in self.graph}
        stack = deque()
        stack.append(start)
        while stack:
            next_node = stack.pop()
            if not self.explored[next_node]:
                self.explored[next_node] = True
                for edge in self.graph[next_node]:
                    stack.append(edge)

    def rdfs(self, start):
        """Run recursive DFS."""
        self.explored[start] = True
        for edge in self.graph[start]:
            if not self.explored[edge]:
                self.rdfs(edge)

    def toposort(self):
        """Run topological sort of a directed graph."""
        self.explored = {k: False for k in self.graph}
        self.cur_label = len(self.graph)
        for v in self.graph:
            if not self.explored[v]:
                self.dfs_topo(v)

    def dfs_topo(self, start):
        """DFS with topological ordering."""
        self.explored[start] = True
        for v in self.graph[start]:
            if not self.explored[v]:
                self.dfs_topo(v)
        self.topo_order[start] = self.cur_label
        self.cur_label -= 1


if __name__ == '__main__':
    undirected = {1: [2, 6],
                  2: [1, 3],
                  3: [2, 4, 5, 6],
                  4: [3, 5],
                  5: [3, 4, 6],
                  6: [1, 3, 5]}

    directed = {1: [2, 3], 2: [4], 3: [4], 4: []}

    print('----- Simple Graph -----')
    graph = Graph(directed)
    # print(graph.explored)
    # graph.rdfs(1)
    print(graph.topo_order)
    graph.toposort()
    print(graph.topo_order)

    # print('----- Karger Graph -----')
    # karger = Graph.read_graph('../karger_mincut.txt')
    # graph = Graph(karger)
    # print(graph.explored)
    # graph.rdfs(1)
    # print(graph.explored)
