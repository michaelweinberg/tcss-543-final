from collections import defaultdict, deque
from adjacency_list import AdjacencyList

def bfs(graph, nodes):
    """
    method running bfs on the graph
    :param graph: current graph (either initial or residual)
    :param nodes: set of all nodes of the graph
    """
    discovered = {node: False for node in nodes}
    discovered['s'] = True
    L = [deque()]
    L[0].append('s')
    i = 0
    tree = AdjacencyList()

    while len(L[i]) > 0:
        L.append(deque())
        while len(L[i]) > 0:
            u = L[i].popleft()
            edges = graph.get(u, [])
            for v in edges:
                if not discovered[v]:
                    discovered[v] = True
                    tree.add_edge(u,v)
                    L[i + 1].append(v)
        i += 1
    return tree