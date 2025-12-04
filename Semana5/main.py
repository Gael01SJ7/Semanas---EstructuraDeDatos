# -----------------------------------------------
# Semana 5 – Proyecto Integrador Avance 3
# Proyecto: Exploración y Análisis del Grafo Urbano

from graph_traversal import GraphTraversal
from pathfinder import PathFinder
from visualize_bfs import draw_bfs_levels

# Definición del grafo urbano
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

print("=== Proyecto Semana 5: BFS y DFS ===\n")

# Crear el grafo
trav = GraphTraversal(directed=False)
for u, vecinos in grafo.items():
    for v in vecinos:
        trav.add_edge(u, v)

pathfinder = PathFinder(trav)

# 1️⃣ BFS básico
print("1. BFS desde A:")
print("Orden BFS:", trav.bfs("A"))

# 2️⃣ DFS básico
print("\n2. DFS desde A:")
print("Orden DFS:", trav.dfs_recursive("A"))

# 3️⃣ Camino más corto
print("\n3. Camino más corto entre A y F:")
print("Camino más corto A→F:", trav.bfs_shortest_path("A", "F"))

# 4️⃣ Componentes conectadas
print("\n4. Componentes conectadas:")
print(trav.find_connected_components())

# 5️⃣ Caso de uso: planificación de rutas
print("\n5. Planificación de rutas de transporte:")
resultado = pathfinder.suggest_route_transport("A", "F")
print("Ruta óptima:", resultado["best"])
print("Alternativas:", resultado["alternatives"])
print("Tiempo estimado (min):", resultado["time_min"])

# 6️⃣ Visualización BFS
print("\nGenerando visualización BFS...")
draw_bfs_levels(trav, "A", title="Niveles BFS desde A")

print("\n✅ Análisis completado correctamente.")
