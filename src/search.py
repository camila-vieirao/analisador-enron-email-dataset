from graph import Graph

class Search:
    def __init__(self, graph: Graph, start_node, end_node, frontier_type):
        self.graph = graph
        self.start_node = start_node
        self.end_node = end_node
        self.frontier_type = frontier_type # bfs ou dfs
        self.frontier = []
        self.explored = set()

    def search(self):
        self.frontier.append((self.start_node, [self.start_node], 0)) # (nó, caminho, custo)
        
        while self.frontier:
            if self.frontier_type == 'bfs':
                current_node, path, cost = self.frontier.pop(0) # FIFO - queue
            elif self.frontier_type == 'dfs':
                current_node, path, cost = self.frontier.pop() # LIFO - stack
            else:
                raise ValueError("frontier_type deve ser 'bfs' ou 'dfs'")

            if current_node == self.end_node:
                return path, cost

            self.explored.add(current_node)

            neighbors = self.graph.visit_neighbors(current_node)
            for neighbor in neighbors:
                if neighbor not in self.explored and all(neighbor != n[0] for n in self.frontier):
                    edge_weight = self.graph.adj[current_node][neighbor]['weight']
                    new_cost = cost + edge_weight
                    new_path = path + [neighbor]
                    self.frontier.append((neighbor, new_path, new_cost))
        return None, float('inf')
    

# TESTE
# if __name__ == "__main__":
#     from parse import parse_emails_to_graph
# 
#     email_dir = "dataset/AmostraEnron/"
#     email_graph = parse_emails_to_graph(email_dir)
# 
#     start = "sandra.brawner@enron.com"
#     end = "drew.fossum@enron.com"
#     search = Search(email_graph, start, end, "bfs")
#     path, cost = search.search()
#     print(f"Caminho: {path}, Custo: {cost}")
# 
#     search2 = Search(email_graph, start, end, "dfs")
#     path2, cost2 = search2.search()
#     print(f"Caminho: {path2}, Custo: {cost2}")