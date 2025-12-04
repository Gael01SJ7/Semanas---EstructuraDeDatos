import heapq
import math
from typing import List, Tuple

class WeightedGraph:
    def __init__(self, n: int, directed: bool = True):
        if n < 0:
            raise ValueError("n must be >= 0")
        self.n = n
        self.directed = directed
        self.adj = {i: [] for i in range(n)}

    def add_edge(self, u: int, v: int, w: float):
        if not (0 <= u < self.n) or not (0 <= v < self.n):
            raise IndexError("node index out of range")
        self.adj[u].append((v, float(w)))
        if not self.directed:
            self.adj[v].append((u, float(w)))

    def dijkstra(self, src: int) -> Tuple[List[float], List[int]]:
        if not (0 <= src < self.n):
            raise IndexError("source node out of range")

        dist = [math.inf] * self.n
        parent = [-1] * self.n
        visited = [False] * self.n

        dist[src] = 0.0
        pq = [(0.0, src)]

        while pq:
            cost, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True

            for v, w in self.adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v))

        return dist, parent

    def floyd_warshall(self) -> Tuple[List[List[float]], List[List[int]]]:
        if self.n == 0:
            raise ValueError("graph empty")

        dist = [[math.inf]*self.n for _ in range(self.n)]
        parent = [[-1]*self.n for _ in range(self.n)]

        for i in range(self.n):
            dist[i][i] = 0
            parent[i][i] = i

        for u in range(self.n):
            for v, w in self.adj[u]:
                dist[u][v] = min(dist[u][v], w)
                parent[u][v] = u

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        parent[i][j] = parent[k][j]

        for i in range(self.n):
            if dist[i][i] < 0:
                raise ValueError("negative cycle detected")

        return dist, parent

    def reconstruct_fw_path(self, parent: List[List[int]], i: int, j: int) -> List[int]:
        if parent[i][j] == -1:
            return []

        path = [j]
        cur = j

        while cur != i:
            cur = parent[i][cur]
            if cur == -1:
                return []
            path.append(cur)

        path.reverse()
        return
