import networkx as nx
import matplotlib.pyplot as plt


def draw_bfs_levels(graph, start, title="Niveles BFS"):
    """Dibuja el grafo con niveles BFS desde un nodo inicial."""
    G = nx.Graph()
    for u, neighbors in graph.adjacency_list.items():
        for v in neighbors:
            G.add_edge(u, v)
 
    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(7, 5))
    nx.draw_networkx_nodes(G, pos, node_color="skyblue", node_size=900)
    nx.draw_networkx_edges(G, pos, edge_color="gray")
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")
    plt.title(title)
    plt.axis("off")
    plt.show()
