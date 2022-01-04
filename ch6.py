from copy import deepcopy
import random


def read_graph(filename):
    adj_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            line = [int(x) for x in line.strip().split()]
            adj_dict[line[0]] = line[1:]
    return adj_dict


def simplify_graph(graph):
    """Remove back-references from the graph."""
    for k, v in graph.items():
        graph[k] = [x for x in v if x > k]
    return graph


def contract_edge(graph, node1, node2):
    graph[node1] = [x for x in graph[node1] if x != node2]
    graph[node2] = [x for x in graph[node2] if x != node1]
    graph[node1] += graph[node2]
    del graph[node2]
    for k, v in graph.items():
        if k != node1:
            graph[k] = [node1 if x == node2 else x for x in graph[k]]
    return graph


def run_karger(graph):
    while len(graph) > 2:
        node1 = random.sample(sorted(graph), k=1)[0]
        node2 = random.sample(graph[node1], k=1)[0]
        graph = contract_edge(graph, node1, node2)
    return len(graph.popitem()[1])


def run_repeated_karger(graph, n=100):
    output = []
    for _ in range(n):
        tmp_graph = deepcopy(graph)
        output.append(run_karger(tmp_graph))
    return min(output)


# graph = {1: [2, 4], 2: [1, 3, 4], 3: [2, 4], 4: [3, 1, 2]}
# contract_edge(graph, 1, 4)

if __name__ == '__main__':
    graph = read_graph('karger_mincut.txt')
    print(run_repeated_karger(graph, n=500))
