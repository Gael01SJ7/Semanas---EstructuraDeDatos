# Semana 5 – Algoritmos de Exploración y Búsqueda

from collections import deque

def bfs(grafo, inicio):
    """Recorre un grafo en amplitud (BFS) desde un nodo inicial."""
    visitados = set()
    cola = deque([inicio])
    orden = []

    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            visitados.add(nodo)
            orden.append(nodo)
            for vecino in grafo.get(nodo, []):
                if vecino not in visitados:
                    cola.append(vecino)

    print("Orden BFS:", " → ".join(orden))
    return orden


if __name__ == "__main__":
    grafo = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "E": ["G"],
        "D": [],
        "F": [],
        "G": []
    }

    print("=== BFS BÁSICO ===")
    bfs(grafo, "A")