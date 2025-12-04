from collections import deque, defaultdict
from enum import Enum
from typing import List, Dict, Set, Optional, Tuple


class NodeState(Enum):
    NOT_VISITED = 0
    IN_PROGRESS = 1
    COMPLETED = 2


class GraphTraversal:
    """Clase que implementa BFS y DFS en grafos."""

    def __init__(self, directed: bool = False):
        self.adjacency_list: Dict[str, List[str]] = defaultdict(list)
        self.directed = directed

    def add_edge(self, u: str, v: str) -> None:
        """Agrega una arista al grafo."""
        self.adjacency_list[u].append(v)
        if not self.directed:
            self.adjacency_list[v].append(u)

   
    # BFS
    def bfs(self, start: str) -> List[str]:
        visited = set([start])
        queue = deque([start])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def bfs_shortest_path(self, start: str, end: str) -> Optional[List[str]]:
        visited = {start}
        parent = {start: None}
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node == end:
                break
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
        if end not in parent:
            return None
        path = []
        node = end
        while node:
            path.append(node)
            node = parent[node]
        path.reverse()
        return path

    # DFS
    def dfs_recursive(self, start: str) -> List[str]:
        visited = set()
        result = []

        def dfs(node):
            visited.add(node)
            result.append(node)
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start)
        return result

    
    # COMPONENTES CONECTADAS
    def find_connected_components(self) -> List[List[str]]:
        visited = set()
        components = []

        def dfs(node, comp):
            visited.add(node)
            comp.append(node)
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, comp)

        for node in self.adjacency_list.keys():
            if node not in visited:
                comp = []
                dfs(node, comp)
                components.append(comp)
        return components
