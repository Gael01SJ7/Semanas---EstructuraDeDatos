def dfs_recursivo(grafo, nodo, visitados=None, orden=None):
    """DFS recursivo."""
    if visitados is None:
        visitados = set()
        orden = []

    visitados.add(nodo)
    orden.append(nodo)

    for vecino in grafo.get(nodo, []):
        if vecino not in visitados:
            dfs_recursivo(grafo, vecino, visitados, orden)

    return orden


def dfs_iterativo(grafo, inicio):
    """DFS iterativo usando pila."""
    pila = [inicio]
    visitados = set()
    orden = []

    while pila:
        nodo = pila.pop()
        if nodo not in visitados:
            visitados.add(nodo)
            orden.append(nodo)
            for vecino in reversed(grafo.get(nodo, [])):
                if vecino not in visitados:
                    pila.append(vecino)
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

    print("=== DFS BÁSICO ===")
    print("Recursivo:", " → ".join(dfs_recursivo(grafo, "A")))
    print("Iterativo:", " → ".join(dfs_iterativo(grafo, "A")))