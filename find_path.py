from bfs import bfs

def find_path(graph, nodes):
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