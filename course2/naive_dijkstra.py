import math


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.nodes_to_inspect = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
        self.lengths = {k: math.inf for k in self.graph}

    @staticmethod
    def read_graph(filename):
        """Read a graph from a text file."""
        tmp_graph = {}
        with open(filename, 'r', encoding='utf8') as f:
            for line in f:
                line = line.strip().split()
                node, edges = line[0], line[1:]
                node = int(node)
                edges = [x.split(',') for x in edges]
                edges = [(int(x[0]), int(x[1])) for x in edges]
                tmp_graph[node] = edges
        return tmp_graph

    def naive_dijkstra(self, start=1):
        """Naive implementation of 'straightforward Dijkstra'"""
        self.lengths[start] = 0
        explored = set()
        not_explored = set(self.graph.keys())
        explored.add(start)
        not_explored.remove(start)
        while not_explored:
            min_length = current_length = math.inf
            for tail in explored:
                for head, length in self.graph[tail]:
                    if head not in explored:
                        current_length = self.lengths[tail] + length
                        if current_length < min_length:
                            min_length = current_length
                            w_star = head
            explored.add(w_star)
            not_explored.remove(w_star)
            self.lengths[w_star] = min_length


if __name__ == '__main__':
    from pprint import pprint
    graph = Graph.read_graph('dijkstra_data.txt')
    graph = Graph(graph)
    # print(graph.graph)
    graph.naive_dijkstra()
    tmp = {k: graph.lengths[k] for k in graph.nodes_to_inspect}
    print(tmp.values())
