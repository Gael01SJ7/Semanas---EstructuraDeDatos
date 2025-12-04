def floyd_warshall(self):
    import math
    INF = math.inf

    dist = [[INF] * self.n for _ in range(self.n)]
    parent = [[None] * self.n for _ in range(self.n)]

    for i in range(self.n):
        dist[i][i] = 0

    for u in range(self.n):
        for v, w in self.adj[u]:
            dist[u][v] = w
            parent[u][v] = u

    for k in range(self.n):
        for i in range(self.n):
            for j in range(self.n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    parent[i][j] = parent[k][j]

    for i in range(self.n):
        if dist[i][i] < 0:
            raise ValueError("Ciclo negativo detectado")

    return dist, parent
