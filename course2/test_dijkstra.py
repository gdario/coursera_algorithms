import unittest
from naive_dijkstra import Graph


class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        simple_graph = {1: [(2, 1), (3, 4)],
                        2: [(3, 2), (4, 6)],
                        3: [(4, 3)],
                        4: []}
        graph = Graph(simple_graph)
        graph.naive_dijkstra()
        self.assertEqual(graph.lengths, {1: 0, 2: 1, 3: 3, 4: 6})
