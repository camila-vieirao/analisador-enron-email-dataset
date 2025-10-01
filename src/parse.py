import os
from .graph import Graph


def parse_emails_to_graph(email_directory):
    """
    Parses emails from the specified directory and constructs a directed graph
    where nodes represent email addresses and edges represent emails sent from
    one address to another.

    Parameters:
    email_directory (str): Path to the directory containing email files.

    Returns:
    Graph: A directed graph representing email communications.
    """
    G = Graph()

    try:
        print("Starting to parse emails...")
        for root, dirs, files in os.walk(email_directory):
            print(f"Processing directory: {root}")
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
                    sender = None
                    to_field = ""
                    in_to = False
                    for line in lines:
                        if line.startswith("From:"):
                            in_to = False
                            sender = line.split("From:")[1].strip()
                        elif line.startswith("To:"):
                            in_to = True
                            to_field = line.split("To:")[1].strip()
                        elif in_to and (line.startswith(" ") or line.startswith("\t")):
                            to_field += " " + line.strip()
                        else:
                            in_to = False
                    if sender and to_field:
                        recipients = [
                            addr.strip() for addr in to_field.split(",") if addr.strip()
                        ]
                        for recipient in recipients:
                            if G.graph_has_edge(sender, recipient):
                                G.adj[sender][recipient]["weight"] += 1
                            else:
                                G.graph_add_edge(sender, recipient, weight=1)
            print(f"Finished processing directory: {root}")
        print(
            f"Graph has {G.graph_number_of_nodes()} nodes and {G.graph_number_of_edges()} edges."
        )
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return G


# TESTE
# if __name__ == "__main__":
#     #email_dir = "dataset/AmostraEnron/"
#     #email_graph = parse_emails_to_graph(email_dir)
#     email_dir = "dataset/AmostraEnron/brawner-s/contract/"
#     email_graph = parse_emails_to_graph(email_dir)
# 
#     print(email_graph.graph_20_highest_out_degree())
#     print("----")
#     print(email_graph.graph_20_highest_in_degree())
