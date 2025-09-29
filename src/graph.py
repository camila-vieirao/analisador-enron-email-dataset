class Graph:
    def __init__(self):
        self.adj = {}
        self.labels = {} # armazenar rotulos (enderecos de email)

    def graph_has_edge(self, node1, node2):
        return node1 in self.adj and node2 in self.adj[node1]

    def graph_add_edge(self, node1, node2, weight=1):
        if node1 not in self.adj:
            self.adj[node1] = {}
        if node2 not in self.adj:
            self.adj[node2] = {}
        self.adj[node1][node2] = {"weight": weight}

    def graph_number_of_nodes(self): # numero de vertices
        return len(self.adj)

    def graph_number_of_edges(self): # numero de arestas
        return sum(len(neighbors) for neighbors in self.adj.values())
