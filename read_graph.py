from collections import defaultdict

def read_graph(file_name):
    nodes = set()
    graph = defaultdict(dict) 
    with open(file_name, 'r') as file:
        for line in file:
            values = line.split()
            if values:                
                u,v,c = values[0], values[1], values[2]
                graph[u][v] = int(c)
                nodes.add(values[0])
                if len(values) > 1:
                    nodes.add(values[1])
    return graph,nodes