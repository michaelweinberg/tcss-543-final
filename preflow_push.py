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

class Graph:

    def __init__(self, V):

        self.V = V;
        self.edge = []
        self.ver = {}

    def addEdge(self, u, v, capacity):

        self.edge.append(Edge(0, capacity, u, v))

    def preflow(self, s):

        self.ver[s].h = len(self.ver);

        for i in range(len(self.edge)):

            if (self.edge[i].u == s):

                self.edge[i].flow = self.edge[i].capacity

                self.ver[self.edge[i].v].e_flow += self.edge[i].flow

                self.edge.append(Edge(-self.edge[i].flow, 0, self.edge[i].v, s))

    def overFlowVertex(self):

        for i in range(1, len(self.ver) - 1):
            thing = self.ver[str(i)].e_flow
            if (self.ver[str(i)].e_flow > 0):
                return str(i)

        return -1

    def updateReverseEdgeFlow(self, i, flow):

        u = self.edge[i].v
        v = self.edge[i].u

        for j in range(0, len(self.edge)):
            if (self.edge[j].v == v and self.edge[j].u == u):
                self.edge[j].flow -= flow
                return

        e = Edge(0, flow, u, v)
        self.edge.append(e)

    def push(self, u):

        for i in range(0, len(self.edge)):

            if (self.edge[i].u == u):

                if (self.edge[i].flow == self.edge[i].capacity):
                    continue;

                if (self.ver[u].h > self.ver[self.edge[i].v].h):

                    flow = min(self.edge[i].capacity - self.edge[i].flow, self.ver[u].e_flow)

                    self.ver[u].e_flow -= flow;

                    self.ver[self.edge[i].v].e_flow += flow;

                    self.edge[i].flow += flow;

                    self.updateReverseEdgeFlow(i, flow);

                    return True;

        return False;

    def relabel(self, u):
        mh = 2100000

        for i in range(len(self.edge)):
            if (self.edge[i].u == u):

                if (self.edge[i].flow == self.edge[i].capacity):
                    continue;

                if (self.ver[self.edge[i].v].h < mh):
                    mh = self.ver[self.edge[i].v].h;

                    self.ver[u].h = mh + 1;

    def getMaxFlow(self, s, t):

        self.preflow(s);
        counter = 0
        while (self.overFlowVertex() != -1):
            counter += 1
            u = self.overFlowVertex();
            if (self.push(u) == False):
                self.relabel(u);

        return self.ver[str(len(self.ver) - 1)].e_flow

    # def parse_pp(self, value, graphType, n):


    def read_graph_pp(self, file_name, graphType, n):

        with open(file_name, 'r') as file:
            for line in file:
                # count = file.readlines()
                values = line.split()
                if values:
                    u, v, c = values[0], values[1], int(values[2])
                    if u not in self.ver:
                        self.ver[u] = (Vertex(0, 0))
                    if v not in self.ver:
                        self.ver[v] = (Vertex(0, 0))
                    if len(values) > 1:
                        self.addEdge(u, v, c)

# V = 402;
# g = Graph(V);

# g.read_graph_pp('../test-graphs/fixedDegree/fixedDegree25.txt')

# Creating above shown flow network
# g.addEdge('0', '1', 16);
# g.addEdge('0', '2', 13);
# g.addEdge('1', '2', 10);
# g.addEdge('2', '1', 4);
# g.addEdge('1', '3', 12);
# g.addEdge('2', '4', 14);
# g.addEdge('3', '2', 9);
# g.addEdge('3', '5', 20);
# g.addEdge('4', '3', 7);
# g.addEdge('4', '5', 4);

# Initialize source and sink
# s = '0'
# t = '401';

# print("Maximum flow is ", g.getMaxFlow(s, t));