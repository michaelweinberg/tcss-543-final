def augment(f, P, graph):
    """
    method augmenting the flow
    :param f: current flow
    :param P: augmenting path
    :param graph: current capacities of the graph
    :return: f - augmented flow, b - bottleneck among the path
    """
    b = float('inf')
    previous = P[0]
    for next in P[1:]:
        if(previous in graph and next in graph[previous] and previous!=next):
            b = min(b, graph[previous][next])
            previous = next
    u = P[0]
    for v in P[1:]:
        f[u][v] += b
        f[v][u] -= b
        u = v
    return f,b