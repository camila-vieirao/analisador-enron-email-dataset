import os
import networkx as nx

def parse_emails_to_graph(email_directory):
    """
    Parses emails from the specified directory and constructs a directed graph
    where nodes represent email addresses and edges represent emails sent from
    one address to another.

    Parameters:
    email_directory (str): Path to the directory containing email files.

    Returns:
    nx.DiGraph: A directed graph representing email communications.
    """
    G = nx.DiGraph()

    try:
        print("Starting to parse emails...")
        for root, dirs, files in os.walk(email_directory):
            print(f"Processing directory: {root}")
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                    sender = None
                    recipients = []
                    for line in lines:
                        if line.startswith("From:"):
                            sender = line.split("From:")[1].strip()
                        elif line.startswith("To:"):
                            recipients = [addr.strip() for addr in line.split("To:")[1].split(", ")]
                        elif line.startswith("Cc:"):
                            cc_recipients = [addr.strip() for addr in line.split("Cc:")[1].split(", ")]
                            recipients.extend(cc_recipients)
                    if sender and recipients:
                        for recipient in recipients:
                            if G.has_edge(sender, recipient):
                                G[sender][recipient]['weight'] += 1
                            else:
                                G.add_edge(sender, recipient, weight=1)
            print(f"Finished processing directory: {root}")
        print(f"Graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return G


# TESTE
# if __name__ == "__main__":
#     email_dir = "dataset/AmostraEnron/"
#     email_graph = parse_emails_to_graph(email_dir)
    