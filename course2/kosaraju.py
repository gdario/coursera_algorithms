from collections import defaultdict, deque, Counter
import sys
import threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)


class Graph:
    def __init__(self, filename):
        self.data = self.read_data(filename)
        self.direct_graph = self.build_direct_graph()
        self.reversed_graph = self.build_reversed_graph()

    def build_direct_graph(self):
        """Build the direct graph from node pairs."""
        graph = defaultdict(list)
        [graph[x[0]].append(x[1]) for x in self.data]
        return graph

    def build_reversed_graph(self):
        """Build the reversed graph from node pairs."""
        graph = defaultdict(list)
        [graph[x[1]].append(x[0]) for x in self.data]
        return graph

    @staticmethod
    def read_data(filename):
        """Read a list of node pairs from a file."""
        with open(filename, 'r', encoding='utf8') as f:
            data = f.read().splitlines()
        data = [[int(x) for x in line.split()] for line in data]
        return data

    @staticmethod
    def extract_nodes(graph):
        """Extract the set of nodes from a graph."""
        nodes = set(graph.keys())
        edges = {x for line in graph.values() for x in line}
        return nodes | edges

    def dfs(self, start):
        """Run DFS on a graph given a starting node."""
        explored = {k: False for k in self.nodes}
        stack = deque()
        stack.append(start)
        while stack:
            v = stack.pop()
            if not explored[v]:
                explored[v] = True
                stack.extend(self.graph[v])
        return explored

    def dfs_topo_iterative(self, start):
        """Run DFS with a given starting node."""
        stack = deque()
        stack.append(start)
        while stack:
            v = stack.pop()
            if not self.explored[v]:
                self.explored[v] = True
                for w in self.graph[v]:
                    stack.append(w)
                    self.topo_order[w] = self.cur_label
                    self.cur_label -= 1

    def toposort(self, graph):
        """Run topological sort of a directed graph."""
        self.nodes = self.extract_nodes(graph)
        self.explored = {k: False for k in self.nodes}
        self.topo_order = {k: -1 for k in self.nodes}
        self.cur_label = len(self.nodes)
        for v in self.nodes:
            if not self.explored[v]:
                self.dfs_topo(graph, v)

    def dfs_topo(self, graph, start):
        """Run recursive DFS with a given starting node."""
        self.explored[start] = True
        for vertex in graph[start]:
            if not self.explored[vertex]:
                self.dfs_topo(graph, vertex)
        self.topo_order[start] = self.cur_label
        self.cur_label -= 1

    def dfs_scc(self, graph, start):
        self.explored[start] = True
        self.scc[start] = self.num_scc
        for w in graph[start]:
            if not self.explored[w]:
                self.dfs_scc(graph, w)

    def kosaraju(self):
        # Run first DFS on the reversed graph
        self.toposort(self.reversed_graph)
        # Reorder the nodes by increasing f-value.
        self.nodes = dict(sorted(self.topo_order.items(), key=lambda x: x[1]))
        # Reset the explored dict
        self.explored = {k: False for k in self.nodes}
        # Reset SCC index for each node
        self.scc = {k: -1 for k in self.nodes}
        # SCC counter
        self.num_scc = 0
        for vertex in self.nodes:
            if not self.explored[vertex]:
                self.num_scc += 1
                self.dfs_scc(self.direct_graph, vertex)


def main():
    FILENAME = 'scc.txt'
    # FILENAME = 'graph_8_16.txt'
    graph = Graph(FILENAME)
    graph.kosaraju()
    print(graph.num_scc)
    scc_counts = Counter(graph.scc.values())
    print(scc_counts.most_common(5))


thread = threading.Thread(target=main)
thread.start()
