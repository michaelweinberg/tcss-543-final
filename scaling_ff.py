import sys
from collections import defaultdict
from turtle import update
from read_graph import read_graph
from adjacency_list import AdjacencyList
from find_path import find_path
from augment import augment

def max_capacity_out_of_s(graph):
    """
    method finding the max capacity of edges going out of s
    :param graph: initial graph
    :return: max capacity
    """
    max_c = 0
    for c in graph['s'].values():
        max_c = max(max_c,c)
    return max_c

def find_delta(graph):
    """
    method finding initial value of delta
    :param graph: initial graph
    :return: initial delta
    """
    delta = 1
    max_c = max_capacity_out_of_s(graph)
    while delta*2 <= max_c:
        delta *= 2
    return delta

def update_r_graph(nodes, capacity, delta):
    """
    method updating residual graph with respect to the current capacities and delta
    :param nodes: set of all nodes of the graph
    :param capacity: current capacities of the graph edges
    :param delta: current delta
    :return: residual graph
    """
    residual_graph = AdjacencyList()
    for u in nodes:
        for v in nodes:
            if(capacity[u][v] >= delta):
                residual_graph.add_edge(u,v)
    return residual_graph   

def scaling_ff(graph, nodes):
    """
    method calculating max flow using scaling Ford Fulkerson algorithm
    :param graph: initial graph
    :param nodes: set of all nodes of the graph
    :return: the max flow of a flow network
    """
    max_flow = 0
    capacity = defaultdict(dict)
    f = defaultdict(dict) 
    for u in nodes:
        for v in nodes:
            f[u][v] = 0
            if u in graph and u != v and v in graph[u]:
                capacity[u][v] = graph[u][v]
            else:
                capacity[u][v] = 0
    delta = find_delta(graph)
    while delta >= 1:
        residual_graph = update_r_graph(nodes, capacity, delta)
        while (path := find_path(residual_graph.adj_list, nodes)) is not None:
            f,b = augment(f, path, capacity)
            for u, v in zip(path, path[1:]):
                capacity[u][v] -= b
                capacity[v][u] += b
            residual_graph = update_r_graph(nodes, capacity, delta)
        delta = delta / 2
    for u in nodes:
        max_flow += f['s'][u]

    return max_flow