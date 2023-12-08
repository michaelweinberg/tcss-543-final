import sys
from collections import defaultdict

import find_path
from adjacency_list import AdjacencyList
from find_path import find_path
from augment import augment
from read_graph import read_graph

def update_r_graph(nodes, capacity):
    """
    method updating residual graph with respect to the current capacities
    :param nodes: set of all nodes of the graph
    :param capacity: current capacities of the graph edges
    :return: residual graph
    """
    residual_graph = AdjacencyList()
    for u in nodes:
        for v in nodes:
            if capacity[u][v] > 0:
                residual_graph.add_edge(u, v)
    return residual_graph

def ff(graph, nodes):
    """
    method calculating max flow using Ford Fulkerson algorithm
    :param graph: initial graph
    :param nodes: set of all nodes of the graph
    :return: the max flow of a flow network
    """
    capacity = defaultdict(dict)
    f = defaultdict(dict)
    for u in nodes:
        for v in nodes:
            f[u][v] = 0
            if u in graph and u != v and v in graph[u]:
                capacity[u][v] = graph[u][v]
            else:
                capacity[u][v] = 0

    residuals = update_r_graph(nodes, capacity)
    while (path := find_path(residuals.adj_list, nodes)) is not None:
        f,b = augment(f, path, capacity)
        for u,v in zip(path, path[1:]):
            capacity[u][v] -= b
            capacity[v][u] += b
        residuals = update_r_graph(nodes, capacity)
    max_flow = 0
    for u in nodes:
        max_flow += f['s'][u]
    return max_flow