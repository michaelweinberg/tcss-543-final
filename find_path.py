from bfs import bfs

def find_path(graph, nodes):
    """
    method finding path from the source to the sink of the graph
    :param graph: current graph (either initial or residual)
    :param nodes: set of all nodes of the graph
    :return: found path
    """
    tree = bfs(graph, nodes)
    tree = tree.reverse()
    path = []
    
    v = 't'
    while (v != 's'):
        path.insert(0,v)
        edges = tree[v]
        if(len(edges) > 0):
            v = edges[0]
        else:
            return
    path.insert(0,v)
    return path