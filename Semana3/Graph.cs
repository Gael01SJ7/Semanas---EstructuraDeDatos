
using System;
using System.Collections.Generic;
using System.Linq;


/// <summary>
/// Grafo genérico dirigido con pesos.
/// Usa lista de adyacencia para eficiencia en memoria.
/// Soporta multiaristas (múltiples aristas entre (u,v) con diferentes pesos).
/// </summary>
public class Graph<T> where T : notnull
{
    private readonly Dictionary<T, List<(T to, double weight)>> adj = new();
    private readonly bool isDirected;

    public Graph(bool directed = true)
    {
        isDirected = directed;
    }

    public void AddVertex(T v)
    {
        if (!adj.ContainsKey(v))
        {
            adj[v] = new List<(T, double)>();
        }
    }

    public void AddEdge(T u, T v, double weight = 1.0)
    {
        AddVertex(u);
        AddVertex(v);

        if (!adj[u].Exists(e => EqualityComparer<T>.Default.Equals(e.to, v) && Math.Abs(e.weight - weight) < 0.0001))
        {
            adj[u].Add((v, weight));
        }

        if (!isDirected)
        {
            if (!adj[v].Exists(e => EqualityComparer<T>.Default.Equals(e.to, u) && Math.Abs(e.weight - weight) < 0.0001))
            {
                adj[v].Add((u, weight));
            }
        }
    }

    public bool HasEdge(T u, T v)
    {
        if (!adj.ContainsKey(u)) return false;

        foreach (var (neighbor, _) in adj[u])
        {
            if (EqualityComparer<T>.Default.Equals(neighbor, v)) return true;
        }
        return false;
    }

    public bool HasEdgeWithWeight(T u, T v, double weight)
    {
        if (!adj.ContainsKey(u)) return false;

        foreach (var (neighbor, w) in adj[u])
        {
            if (EqualityComparer<T>.Default.Equals(neighbor, v) && Math.Abs(w - weight) < 0.0001)
            {
                return true;
            }
        }
        return false;
    }

    public IEnumerable<(T to, double weight)> Neighbors(T u)
    {
        if (!adj.ContainsKey(u))
        {
            throw new ArgumentException($"Vértice {u} no existe en el grafo");
        }
        return adj[u];
    }

    public int OutDegree(T u)
    {
        return adj.ContainsKey(u) ? adj[u].Count : 0;
    }

    public int InDegree(T v)
    {
        int count = 0;
        foreach (var u_neighbors in adj.Values)
        {
            count += u_neighbors.Count(e => EqualityComparer<T>.Default.Equals(e.to, v));
        }
        return count;
    }

    public int RemoveEdge(T u, T v)
    {
        int removed = 0;
        if (adj.ContainsKey(u))
        {
            removed = adj[u].RemoveAll(e => EqualityComparer<T>.Default.Equals(e.to, v));
        }

        if (!isDirected && adj.ContainsKey(v))
        {
            adj[v].RemoveAll(e => EqualityComparer<T>.Default.Equals(e.to, u));
        }

        return removed;
    }

    public bool RemoveEdgeWithWeight(T u, T v, double weight)
    {
        bool removed = false;

        if (adj.ContainsKey(u))
        {
            int index = adj[u].FindIndex(e =>
                EqualityComparer<T>.Default.Equals(e.to, v) &&
                Math.Abs(e.weight - weight) < 0.0001);

            if (index >= 0)
            {
                adj[u].RemoveAt(index);
                removed = true;
            }
        }

        if (!isDirected && adj.ContainsKey(v))
        {
            int index = adj[v].FindIndex(e =>
                EqualityComparer<T>.Default.Equals(e.to, u) &&
                Math.Abs(e.weight - weight) < 0.0001);

            if (index >= 0)
            {
                adj[v].RemoveAt(index);
            }
        }

        return removed;
    }

    public bool RemoveVertex(T v)
    {
        if (!adj.ContainsKey(v)) return false;

        foreach (var u in adj.Keys.ToList())
        {
            adj[u].RemoveAll(e => EqualityComparer<T>.Default.Equals(e.to, v));
        }

        adj.Remove(v);
        return true;
    }

    public IEnumerable<T> Vertices() => adj.Keys;
    public int VertexCount() => adj.Count;

    public int EdgeCount()
    {
        int count = adj.Values.Sum(list => list.Count);
        return isDirected ? count : count / 2;
    }

    public List<double> GetEdgeWeights(T u, T v)
    {
        if (!adj.ContainsKey(u)) return new List<double>();

        return adj[u]
            .Where(e => EqualityComparer<T>.Default.Equals(e.to, v))
            .Select(e => e.weight)
            .ToList();
    }

    public void Print()
    {
        Console.WriteLine($"Grafo {(isDirected ? "dirigido" : "no dirigido")} con {VertexCount()} vértices y {EdgeCount()} aristas:");
        foreach (var u in adj.Keys.OrderBy(k => k.ToString()))
        {
            Console.Write($"{u} → ");
            foreach (var (v, w) in adj[u])
            {
                Console.Write($"({v}, {w:F1}) ");
            }
            Console.WriteLine();
        }
    }
}
