class Graph:
    def __init__(self):
        self.adj = {}

    def graph_has_edge(self, node1, node2):
        return node1 in self.adj and node2 in self.adj[node1]

    def graph_add_edge(self, node1, node2, weight=1):
        if node1 not in self.adj:
            self.adj[node1] = {}
        if node2 not in self.adj:
            self.adj[node2] = {}
        self.adj[node1][node2] = {"weight": weight}

    def graph_number_of_nodes(self):  # numero de vertices
        return len(self.adj)

    def graph_number_of_edges(self):  # numero de arestas
        return sum(len(neighbors) for neighbors in self.adj.values())

    def graph_20_highest_out_degree(self):  # 20 individuos com maior grau de saida
        out_degrees = {node: len(neighbors) for node, neighbors in self.adj.items()}
        sorted_out_degrees = sorted(
            out_degrees.items(), key=lambda x: x[1], reverse=True
        )
        return sorted_out_degrees[:20]

    def graph_20_highest_in_degree(self):  # 20 individuos com maior grau de entrada
        in_degrees = {node: 0 for node in self.adj}
        for neighbors in self.adj.values():
            for neighbor in neighbors:
                in_degrees[neighbor] += 1
        sorted_in_degrees = sorted(in_degrees.items(), key=lambda x: x[1], reverse=True)
        return sorted_in_degrees[:20]
    
    def visit_neighbors(self, node):
        if node in self.adj:
            return list(self.adj[node].keys())
        return []
