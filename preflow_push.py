from read_graph import Edge, Vertex
class Graph:
    """
    Class to represent a directed graph
    """
    def __init__(self, vertices, edges):
        """
        :param vertices: verices in the graph
        :param edges: edges in the graph
        """
        self.vertices = vertices
        self.edges = edges


    def add_edge(self, u, v, capacity):
        """
        method to add an edge to the graph
        :param u: the source vertex of a directed edge
        :param v: the destination vertex of a directed edge
        :param capacity: the capacity of the edge
        """
        self.edges.append(Edge(0, capacity, u, v))

    def preflow(self, s):
        """
        method to initialize heights and flows in the flow network
        :param s: the sink node in the graph
        """

        self.vertices[s].height = len(self.vertices);

        for i in range(len(self.edges)):

            if (self.edges[i].u == s):

                self.edges[i].flow = self.edges[i].capacity

                self.vertices[self.edges[i].v].excess_flow += self.edges[i].flow

                self.edges.append(Edge(-self.edges[i].flow, 0, self.edges[i].v, s))

    def overflow_vertex(self, s, t):
        """
        method to identify vertex to push excess flow to
        :param s: the source vertex
        :param t: the sink vertex
        :return: the key representing the vertex representing t
                he vertex being evaluated or -1 representing there
                is none and the algorithm has found max flow

        """

        for key in self.vertices:
            if (self.vertices[key].excess_flow > 0 and key != s and key != t):
                return key

        return -1

    def update_reverse_edge_flow(self, i, flow):
        """
        update the reverse flow on the reverse edge in the residual graph
        :param i: the index of the edge to reverse flow
        :param flow: the amount of flow to push in reverse
        """

        u = self.edges[i].v
        v = self.edges[i].u

        for j in range(0, len(self.edges)):
            if (self.edges[j].v == v and self.edges[j].u == u):
                self.edges[j].flow -= flow
                return

        e = Edge(0, flow, u, v)
        self.edges.append(e)

    def push(self, u):
        """
        :param u: the vertex the flow is being pushed from
        :return: boolean of whether or not to continue pushing
                flow
        """

        for i in range(0, len(self.edges)):

            if (self.edges[i].u == u):

                if (self.edges[i].flow == self.edges[i].capacity):
                    continue;

                if (self.vertices[u].height > self.vertices[self.edges[i].v].height):

                    flow = min(self.edges[i].capacity - self.edges[i].flow, self.vertices[u].excess_flow)

                    self.vertices[u].excess_flow -= flow;

                    self.vertices[self.edges[i].v].excess_flow += flow;

                    self.edges[i].flow += flow;

                    self.update_reverse_edge_flow(i, flow);

                    return True;

        return False;

    def relabel(self, u):
        """
        relabel a vertex
        :param u: the vertex to be relabeled
        """
        mh = 2100000

        for i in range(len(self.edges)):
            if (self.edges[i].u == u):

                if (self.edges[i].flow == self.edges[i].capacity):
                    continue;

                if (self.vertices[self.edges[i].v].height < mh):
                    mh = self.vertices[self.edges[i].v].height;

                    self.vertices[u].height = mh + 1;

    def getMaxFlow(self, s, t):
        """
        master method to retrieve max flow
        :param s: source vertex
        :param t: sink vertex
        :return: the max flow of a flow network
        """

        self.preflow(s);
        while (self.overflow_vertex(s, t) != -1):
            u = self.overflow_vertex(s, t);
            if (self.push(u) == False):
                self.relabel(u);

        return self.vertices['t'].excess_flow

def preflow_push(vertices, edges):
    """
    function to import that will instatiate the flow network and return a max flow
    :param vertices: the vertices in a flow network
    :param edges: the edges in a flow network
    :return: and integer representing the max flow of a flow network
    """
    s = 's'
    t = 't';
    g = Graph(vertices, edges);
    return g.getMaxFlow(s, t)

"""
CITATIONS: 
https://www.geeksforgeeks.org/push-relabel-algorithm-set-2-implementation/
"""
