def dfs(grafo, nodo, visitados, componente):
    visitados.add(nodo)
    componente.append(nodo)
    for vecino in grafo.get(nodo, []):
        if vecino not in visitados:
            dfs(grafo, vecino, visitados, componente)


def componentes(grafo):
    """Encuentra componentes conectadas en grafo no dirigido."""
    visitados = set()
    resultado = []

    for nodo in grafo:
        if nodo not in visitados:
            comp = []
            dfs(grafo, nodo, visitados, comp)
            resultado.append(comp)

    print(f"Número de componentes: {len(resultado)}")
    for i, c in enumerate(resultado, 1):
        print(f"Componente {i}: {', '.join(c)}")
    return resultado


if __name__ == "__main__":
    grafo = {
        "1": ["2", "3"],
        "2": ["1", "3"],
        "3": ["1", "2"],
        "4": ["5"],
        "5": ["4"],
        "6": ["7", "8"],
        "7": ["6", "8"],
        "8": ["6", "7"]
    }

    print("=== COMPONENTES CONECTADAS ===")
    componentes(grafo)