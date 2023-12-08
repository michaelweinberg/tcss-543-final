from collections import defaultdict

class Edge:

    def __init__(self, flow, capacity, u, v):
        self.flow = flow
        self.capacity = capacity
        self.u = u
        self.v = v
class Vertex:

    def __init__(self, h, e_flow):
        self.h = h
        self.e_flow = e_flow
def read_graph(file_name, graph_type):
    if graph_type == "preflow_push":
        nodes = []
    else:
        nodes = set()
    graph = defaultdict(dict) 
    with open(file_name, 'r') as file:
        for line in file:
            values = line.split()
            if values:                
                u,v,c = values[0], values[1], values[2]
                if graph_type == "preflow_push":
                    nodes.append(Edge(0, int(c), u, v))
                    if u not in graph:
                        graph[u] = (Vertex(0, 0))
                    if v not in graph:
                        graph[v] = (Vertex(0, 0))
                else:
                    graph[u][v] = int(c)
                    nodes.add(values[0])
                    if len(values) > 1:
                        nodes.add(values[1])

    return graph,nodes