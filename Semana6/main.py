from weighted_graph import WeightedGraph

g = WeightedGraph(5, directed=True)

g.add_edge(0, 1, 4)
g.add_edge(0, 2, 2)
g.add_edge(1, 2, 5)
g.add_edge(1, 3, 10)
g.add_edge(2, 4, 3)
g.add_edge(4, 3, 4)

dist, parent = g.dijkstra(0)
print("=== DIJKSTRA DESDE 0 ===")
print("Distancias:", dist)

from_node = 0
to_node = 3
ruta = g.reconstruct_path(parent, from_node, to_node)
print("Ruta óptima 0 -> 3:", ruta)

fw, p = g.floyd_warshall()
print("\n=== FLOYD-WARSHALL ===")
for fila in fw:
    print(fila)

ruta_fw = g.reconstruct_fw_path(p, 0, 3)
print("\nRuta FW 0 -> 3:", ruta_fw)
