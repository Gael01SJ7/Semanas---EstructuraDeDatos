import random
from typing import Dict, List
from graph_traversal import GraphTraversal


class PathFinder:
    """Caso de uso: planificación de rutas de transporte."""

    def __init__(self, graph: GraphTraversal):
        self.graph = graph

    def suggest_route_transport(self, origen: str, destino: str) -> Dict[str, List[str]]:
        """Sugiere rutas y tiempo estimado entre dos puntos."""
        best_path = self.graph.bfs_shortest_path(origen, destino)
        if not best_path:
            return {"best": None, "alternatives": [], "time_min": 0}

        # Crear rutas alternativas
        alternatives = []
        for i in range(len(best_path) - 1):
            partial = best_path[:i] + best_path[i + 1 :]
            if len(partial) > 2:
                alternatives.append(partial)

        # Simular tiempos (5 a 10 minutos por tramo)
        time_min = (len(best_path) - 1) * random.randint(5, 10)

        return {
            "best": best_path,
            "alternatives": alternatives,
            "time_min": time_min,
        }
