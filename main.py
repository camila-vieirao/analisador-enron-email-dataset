from src.parse import parse_emails_to_graph
from src.search import Search

def main():
    email_dir = "dataset/AmostraEnron/"
    email_graph = parse_emails_to_graph(email_dir)
    print("")
    print("-----------------------------------------------------")
    print("parsing completo")
    print("")
    
    email_graph.graph_number_of_nodes()
    email_graph.graph_number_of_edges()
    email_graph.graph_20_highest_out_degree()
    email_graph.graph_20_highest_in_degree()
    print(f"Número de vértices: {email_graph.graph_number_of_nodes()}")
    print(f"Número de arestas: {email_graph.graph_number_of_edges()}")
    print("20 indivíduos com maior grau de saída:", email_graph.graph_20_highest_out_degree())
    print("20 indivíduos com maior grau de entrada:", email_graph.graph_20_highest_in_degree())
    print("-----------------------------------------------------")

    print("")
    print("busca:")
    start = "sandra.brawner@enron.com"
    end = "drew.fossum@enron.com"
    search = Search(email_graph, start, end, "bfs")
    path, cost = search.search()
    print(f"Caminho: {path}, Custo: {cost}")

    search2 = Search(email_graph, start, end, "dfs")
    path2, cost2 = search2.search()
    print(f"Caminho: {path2}, Custo: {cost2}")

    print("")
    print("busca completa")
    print("----------------------------------------------------")
    
    print("")
    print("nos que estao a uma distancia D de N:")
    all_neighbors = email_graph.all_neighbors_given_distance("sandra.brawner@enron.com", 4)
    print(all_neighbors)
    print("----------------------------------------------------")

if __name__ == "__main__":
    main()