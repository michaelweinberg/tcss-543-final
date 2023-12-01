from collections import defaultdict, deque
from turtle import update
from read_graph import read_graph
from adjacency_list import AdjacencyList
from find_path import find_path
from augment import augment

def max_capacity_out_of_s(graph):
    max_c = 0
    for c in graph['s'].values():
        max_c = max(max_c,c)
    return max_c

def find_delta(graph):
    delta = 1
    max_c = max_capacity_out_of_s(graph)
    while delta*2 <= max_c:
        delta *= 2
    return delta

def update_r_graph(nodes, capacity, delta):
    residual_graph = AdjacencyList()
    for u in nodes:
        for v in nodes:
            if(capacity[u][v] >= delta):
                residual_graph.add_edge(u,v)
    return residual_graph   

def scaling_m_f(graph, nodes):
    max_flow = 0
    current_flow = 0
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
        path = find_path(residual_graph.adj_list, nodes)
        while path:
            f,b = augment(f, path, capacity)
            for u, v in zip(path, path[1:]):
                capacity[u][v] -= b
                capacity[v][u] += b
                residual_graph = update_r_graph(nodes, capacity, delta)
                    
            path = find_path(residual_graph.adj_list, nodes)
        delta = delta / 2
    for u in nodes:
        if (f['s'][u] != 0):
            max_flow = max_flow + f['s'][u]
    current_flow = max_flow - current_flow

    return max_flow  

file_name = input("Enter the name of the graph file: ")
graph,nodes = read_graph(file_name)
max_flow = scaling_m_f(graph, nodes)
print("Max Flow: ", max_flow)