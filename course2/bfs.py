from collections import deque
import math


class Graph:
    def __init__(self, filename):
        self.graph = self.read_graph(filename)
        self.cc = self.ucc()

    def read_graph(self, filename):
        """Read a graph provided as an adjacency list."""
        adj_dict = {}
        with open(filename, 'r') as f:
            for line in f:
                line = [int(x) for x in line.strip().split()]
                adj_dict[line[0]] = line[1:]
        return adj_dict

    def bfs(self, start):
        """Run BFS given a graph and a starting node and return the shortest
        distand of each node from the start node."""
        assert isinstance(start, int), "start must be an integer"
        explored = {k: False for k in self.graph}
        dist = {k: math.inf for k in self.graph}
        dist[start] = 0
        queue = deque()
        queue.appendleft(start)
        while queue:
            node = queue.pop()
            for edge in self.graph[node]:
                if not explored[edge]:
                    explored[edge] = True
                    queue.appendleft(edge)
                    dist[edge] = dist[node] + 1
        return dist

    def ucc(self):
        """Implements the Undirected Connected Components algorithm."""
        explored = {k: False for k in self.graph}
        self.num_cc = 0
        self.cc = {k: 0 for k in self.graph}
        for node in self.graph:
            if not explored[node]:
                self.num_cc += 1
                queue = deque()
                queue.appendleft(node)
                while queue:
                    v = queue.pop()
                    self.cc[v] = self.num_cc
                    for w in self.graph[v]:
                        if not explored[w]:
                            explored[w] = True
                            queue.appendleft(w)


if __name__ == '__main__':
    graph = Graph('../karger_mincut.txt')
    graph.ucc()
    print(graph.num_cc)
