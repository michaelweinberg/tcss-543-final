from collections import defaultdict

class AdjacencyList:
    """
    Class to represent an adjacency list of a graph
    """
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        """
        method to add an edge
        :param u: the source vertex of a directed edge
        :param v: the destination vertex of a directed edge
        """
        if(v not in self.adj_list[u]):
            self.adj_list[u].append(v)
    
    def delete_edge(self, u, v):
        """
        method to delete an edge
        :param u: the source vertex of a directed edge
        :param v: the destination vertex of a directed edge
        """
        if v in self.adj_list[u]:
            self.adj_list[u].remove(v)

    def reverse(self):
        """
        method to reverse an adjacency list
        """
        reversed_adj_list = defaultdict(list)

        for u in self.adj_list:
            for v in self.adj_list[u]:
                reversed_adj_list[v].append(u)

        self.adj_list = reversed_adj_list
        return self.adj_list