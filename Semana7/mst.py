"""mst.py
Implementación de Prim y Kruskal con Union-Find (path compression + union by rank).
Uso: python3 mst.py
Contiene: GraphMST class, ejemplos y pruebas básicas.
"""
import heapq

class GraphMST:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []  # Para Kruskal: lista de (u, v, w)
        self.adj = {i: [] for i in range(vertices)}  # Para Prim

    def add_edge(self, u, v, w):
        if u == v:
            return
        # Normalizar orden para facilitar evitare duplicados en algunos usos
        self.edges.append((u, v, w))
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    # --- PRIM ---
    def prim_mst(self, start_node=0):
        visited = [False] * self.V
        pq = []
        visited[start_node] = True
        for neighbor, weight in self.adj[start_node]:
            heapq.heappush(pq, (weight, start_node, neighbor))

        mst_edges = []
        mst_cost = 0
        while pq:
            weight, u, v = heapq.heappop(pq)
            if visited[v]:
                continue
            visited[v] = True
            mst_edges.append((u, v, weight))
            mst_cost += weight
            for nxt, w in self.adj[v]:
                if not visited[nxt]:
                    heapq.heappush(pq, (w, v, nxt))
        # Si el grafo no es conexo, prim_mst no cubrirá todos los nodos
        return mst_edges, mst_cost

    # --- UNION-FIND (DSU) ---
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n

        def find(self, i):
            if self.parent[i] != i:
                self.parent[i] = self.find(self.parent[i])
            return self.parent[i]

        def union(self, i, j):
            ri = self.find(i)
            rj = self.find(j)
            if ri == rj:
                return False
            if self.rank[ri] < self.rank[rj]:
                self.parent[ri] = rj
            elif self.rank[ri] > self.rank[rj]:
                self.parent[rj] = ri
            else:
                self.parent[rj] = ri
                self.rank[ri] += 1
            return True

    # --- KRUSKAL ---
    def kruskal_mst(self):
        dsu = GraphMST.DSU(self.V)
        sorted_edges = sorted(self.edges, key=lambda x: x[2])
        mst_edges = []
        mst_cost = 0
        for u, v, w in sorted_edges:
            if dsu.union(u, v):
                mst_edges.append((u, v, w))
                mst_cost += w
        return mst_edges, mst_cost

# --- pruebas rápidas ---
if __name__ == '__main__':
    # Ejemplo conocido
    g = GraphMST(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    edges_p, cost_p = g.prim_mst()
    edges_k, cost_k = g.kruskal_mst()

    print("Prim MST edges:", edges_p, "Cost:", cost_p)
    print("Kruskal MST edges:", edges_k, "Cost:", cost_k)