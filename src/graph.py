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

    def all_neighbors_given_distance(self, node, distance):
        if distance < 0:
            return set()

        frontier = [(node, 0)]  # (nó, distância)
        explored = set([node])
        exact_distance_nodes = set()

        if distance == 0:
            return {node}

        while frontier:
            current_node, current_distance = frontier.pop(0)  # BFS - FIFO

            if current_distance < distance:
                neighbors = self.visit_neighbors(current_node)
                for neighbor in neighbors:
                    if neighbor not in explored:
                        explored.add(neighbor)
                        new_distance = current_distance + 1
                        frontier.append((neighbor, new_distance))
                        if new_distance == distance:
                            exact_distance_nodes.add(neighbor)

        return exact_distance_nodes