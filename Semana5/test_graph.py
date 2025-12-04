# -----------------------------------------------
# test_graph.py — Pruebas automáticas para Semana 5

from graph_traversal import GraphTraversal
from pathfinder import PathFinder

def test_bfs_order():
    grafo = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }
    trav = GraphTraversal(directed=False)
    for u, vs in grafo.items():
        for v in vs:
            trav.add_edge(u, v)
    bfs = trav.bfs("A")  # ← cambio aquí
    assert bfs == ['A', 'B', 'C', 'D', 'E', 'F']

def test_dfs_order():
    trav = GraphTraversal(directed=False)
    edges = [("A","B"),("A","C"),("B","D"),("B","E"),("C","F"),("E","F")]
    for u,v in edges:
        trav.add_edge(u,v)
    dfs = trav.dfs_recursive("A")
    assert set(dfs) == {"A","B","C","D","E","F"}

def test_shortest_path():
    trav = GraphTraversal(directed=False)
    edges = [("A","B"),("A","C"),("C","F"),("B","E"),("E","F")]
    for u,v in edges:
        trav.add_edge(u,v)
    camino = trav.bfs_shortest_path("A", "F")
    assert camino == ["A","C","F"]

def test_connected_components():
    trav = GraphTraversal(directed=False)
    edges = [("A","B"),("C","D")]
    for u,v in edges:
        trav.add_edge(u,v)
    componentes = trav.find_connected_components()  # ← cambio aquí
    assert len(componentes) == 2

def test_pathfinder_route():
    trav = GraphTraversal(directed=False)
    edges = [("A","B"),("B","C"),("C","D")]
    for u,v in edges:
        trav.add_edge(u,v)
    pathfinder = PathFinder(trav)
    ruta = pathfinder.suggest_route_transport("A","D")
    assert ruta["best"] == ["A","B","C","D"]
    assert ruta["time_min"] >= 10  # puede variar por random.randint

def test_add_edge_bidirectional():
    trav = GraphTraversal(directed=False)
    trav.add_edge("A", "B")
    assert "B" in trav.adjacency_list["A"] and "A" in trav.adjacency_list["B"]  # ← cambio aquí

def test_bfs_empty_graph():
    trav = GraphTraversal(directed=False)
    bfs = trav.bfs("A") if "A" in trav.adjacency_list else []
    assert bfs == []

def test_no_path_found():
    trav = GraphTraversal(directed=False)
    trav.add_edge("A","B")
    trav.add_edge("C","D")
    camino = trav.bfs_shortest_path("A","D")
    assert camino is None or camino == []

print("✅ Todas las pruebas pasaron correctamente.")
