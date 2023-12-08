from collections import defaultdict

class Edge:
    """
    A class representing and edge in the graph
    of the flow network
    """
    def __init__(self, flow, capacity, u, v):
        """
        :param flow: the amount of flow going through the edge
        :param capacity: the capacity of the edge
        :param u: the source vertex of a directed edge
        :param v: the destination vertex of a directed edge
        """
        self.flow = flow
        self.capacity = capacity
        self.u = u
        self.v = v
class Vertex:
    """
    A class representing a Vertex in the graph
    """
    def __init__(self, height, excess_flow):
        """
        :param height: the height of a vertex
        :param excess_flow: the excess flow of a vertex
        """
        self.height = height
        self.excess_flow = excess_flow

def read_graph(file_name, algo_type):
    """
    method reading graph from a file 
    :param file_name: path to and name of the file containing graph info
    :param graph_type: type of the algorithm
    :return: graph and set of its nodes
    """
    if algo_type == "preflow_push":
        nodes = []
    else:
        nodes = set()
    graph = defaultdict(dict) 
    with open(file_name, 'r') as file:
        for line in file:
            values = line.split()
            if values:                
                u,v,c = values[0], values[1], values[2]
                if algo_type == "preflow_push":
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