# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import Dict, List, Tuple, Optional

class Graph:

    """
    Clase para representar un grafo dirigido/no dirigido ponderado con multiaristas.
    Usa defaultdict(list) internamente para eficiencia.
    """
    def __init__(self, directed: bool = True):
        self.adj: Dict[str, List[Tuple[str, float]]] = defaultdict(list)
        self._directed = directed

GraphType = Graph  # Alias para consistencia con funciones antiguas

def create_graph(directed: bool = True) -> GraphType:
    """
    Crea un nuevo grafo vacío.
    
    Args:
        directed: True para grafo dirigido, False para no dirigido
    
    Returns:
        Instancia de Graph
    """
    return Graph(directed)

def add_vertex(graph: GraphType, v: str) -> None:
    """
    Agrega un vértice al grafo si no existe.
    Complejidad: O(1)
    
    Args:
        graph: El grafo donde agregar
        v: Identificador del vértice
    """
    if v not in graph.adj:
        graph.adj[v] = []

def add_edge(graph: GraphType, u: str, v: str, weight: float = 1.0) -> None:
    """
    Agrega una arista al grafo. Soporta multiaristas.
    Previene solo duplicados exactos (mismo u, v, y peso).
    Complejidad: O(grado(u)) por verificación de duplicados
    
    Args:
        graph: El grafo donde agregar
        v: Vértice destino
        weight: Peso de la arista (default: 1.0)
    """
    # Asegurar que ambos vértices existan
    add_vertex(graph, u)
    add_vertex(graph, v)
    
    # Verificar duplicado por (neighbor, weight) con tolerancia para floats
    if not any(neighbor == v and abs(w - weight) < 1e-9 for neighbor, w in graph.adj.get(u, [])):
        graph.adj[u].append((v, weight))
    
    # Si el grafo NO es dirigido, agregar arista inversa
    if not graph._directed:
        if not any(neighbor == u and abs(w - weight) < 1e-9 for neighbor, w in graph.adj.get(v, [])):
            graph.adj[v].append((u, weight))

def has_edge(graph: GraphType, u: str, v: str) -> bool:
    """
    Verifica si existe AL MENOS UNA arista entre u y v (ignora pesos).
    Complejidad: O(grado(u))
    
    Args:
        graph: El grafo a consultar
        u: Vértice origen
        v: Vértice destino
    
    Returns:
        True si existe la arista, False en caso contrario
    """
    if u not in graph.adj:
        return False
    
    # Buscar cualquier arista al destino v
    return any(neighbor == v for neighbor, w in graph.adj[u])

def has_edge_with_weight(graph: GraphType, u: str, v: str, weight: float) -> bool:
    """
    Verifica si existe una arista u→v con el peso exacto (útil para multigrafos).
    Complejidad: O(grado(u))
    
    Args:
        graph: El grafo a consultar
        u: Vértice origen
        v: Vértice destino
        weight: Peso exacto a verificar
    
    Returns:
        True si existe, False en caso contrario
    """
    if u not in graph.adj:
        return False
    
    # Buscar con tolerancia para floats
    return any(neighbor == v and abs(w - weight) < 1e-9 for neighbor, w in graph.adj.get(u, []))

def neighbors(graph: GraphType, u: str) -> List[Tuple[str, float]]:
    """
    Obtiene todos los vecinos de un vértice.
    Complejidad: O(1)
    
    Args:
        graph: El grafo a consultar
        u: Vértice a consultar
    
    Returns:
        Lista de tuplas (vecino, peso)
    
    Raises:
        KeyError: Si el vértice no existe
    """
    if u not in graph.adj:
        raise KeyError(f"Vértice {u} no existe en el grafo")
    return graph.adj[u]

def out_degree(graph: GraphType, u: str) -> int:
    """
    Calcula el grado de salida de un vértice (considera multiaristas).
    Complejidad: O(1)
    
    Args:
        graph: El grafo a consultar
        u: Vértice a consultar
    
    Returns:
        Número de aristas salientes
    """
    return len(graph.adj.get(u, []))

def in_degree(graph: GraphType, v: str) -> int:
    """
    Calcula el grado de entrada de un vértice (considera multiaristas).
    Complejidad: O(n + m)
    
    Args:
        graph: El grafo a consultar
        v: Vértice a consultar
    
    Returns:
        Número de aristas entrantes
    """
    count = 0
    # Revisar todos los vértices
    for u_neighbors in graph.adj.values():
        # Contar cuántas veces aparece v en la lista de vecinos de u
        count += sum(1 for neighbor, w in u_neighbors if neighbor == v)
    return count

def remove_edge(graph: GraphType, u: str, v: str) -> int:
    """
    Elimina TODAS las aristas u→v (incluyendo multiaristas).
    Complejidad: O(grado(u))
    
    Args:
        graph: El grafo a modificar
        u: Vértice origen
        v: Vértice destino
    
    Returns:
        Número de aristas eliminadas.
    """
    removed_count = 0
    
    # Eliminar todas las aristas u → v
    if u in graph.adj:
        original_len = len(graph.adj[u])
        graph.adj[u] = [(neighbor, w) for neighbor, w in graph.adj[u] if neighbor != v]
        removed_count = original_len - len(graph.adj[u])
    
    # Si no es dirigido, eliminar también todas v → u
    if not graph._directed and v in graph.adj:
        original_len_v = len(graph.adj[v])
        graph.adj[v] = [(neighbor, w) for neighbor, w in graph.adj[v] if neighbor != u]
        # No se suma a removed_count para no contar doble
    
    return removed_count

def remove_edge_with_weight(graph: GraphType, u: str, v: str, weight: float) -> bool:
    """
    Elimina LA PRIMERA arista u→v con peso exacto.
    Complejidad: O(grado(u))
    
    Args:
        graph: El grafo a modificar
        u: Vértice origen
        v: Vértice destino
        weight: Peso exacto a eliminar
    
    Returns:
        True si se eliminó, False si no existía
    """
    removed = False
    
    # Eliminar primera coincidencia u → v con peso
    if u in graph.adj:
        for i, (neighbor, w) in enumerate(graph.adj[u]):
            if neighbor == v and abs(w - weight) < 1e-9:
                del graph.adj[u][i]
                removed = True
                break
    
    # Si no es dirigido, eliminar también v → u con mismo peso
    if not graph._directed and v in graph.adj:
        for i, (neighbor, w) in enumerate(graph.adj[v]):
            if neighbor == u and abs(w - weight) < 1e-9:
                del graph.adj[v][i]
                break
    
    return removed

def get_edge_weights(graph: GraphType, u: str, v: str) -> List[float]:
    """
    Obtiene todos los pesos de las aristas u→v (útil para multigrafos).
    Complejidad: O(grado(u))
    
    Args:
        graph: El grafo a consultar
        u: Vértice origen
        v: Vértice destino
    
    Returns:
        Lista de pesos (vacía si no hay aristas)
    """
    if u not in graph.adj:
        return []
    return [w for neighbor, w in graph.adj.get(u, []) if neighbor == v]

def load_graph(path: str, directed: bool = True) -> GraphType:
    """
    Carga un grafo desde un archivo de texto.
    
    Formato del archivo:
        # Comentarios (líneas que empiezan con #)
        u v peso
        u v peso
        ...
    
    Complejidad: O(m * grado_promedio) donde m = número de aristas
    
    Args:
        path: Ruta al archivo
        directed: True para grafo dirigido, False para no dirigido
    
    Returns:
        Grafo cargado desde el archivo
    
    Raises:
        FileNotFoundError: Si el archivo no existe
        ValueError: Si hay líneas con formato inválido
    """
    graph = create_graph(directed)
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                # Eliminar espacios en blanco al inicio y final
                line = line.strip()
                
                # Ignorar líneas vacías y comentarios
                if not line or line.startswith('#'):
                    continue
                
                # Dividir la línea en partes
                parts = line.split()
                
                # Validar formato mínimo: u v [peso]
                if len(parts) < 2:
                    raise ValueError(f"Línea {line_num}: formato inválido '{line}'")
                
                # Extraer vértices
                u, v = parts[0], parts[1]
                
                # Extraer peso (opcional, default = 1.0)
                try:
                    weight = float(parts[2]) if len(parts) > 2 else 1.0
                except ValueError:
                    raise ValueError(f"Línea {line_num}: peso inválido '{parts[2]}'")
                
                # Agregar la arista (con prevención de duplicados)
                add_edge(graph, u, v, weight) # La función add_edge maneja el caso no dirigido
        
        return graph
    
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo: {path}")

def print_graph(graph: GraphType) -> None:
    """
    Imprime el grafo de forma legible.
    
    Args:
        graph: El grafo a imprimir
    """
    tipo = "dirigido" if graph._directed else "no dirigido"
    num_vertices = len(graph.adj)
    num_aristas = sum(len(vecinos) for vecinos in graph.adj.values())
    if not graph._directed:
        num_aristas //= 2  # Cada arista se cuenta dos veces
    
    print(f"Grafo {tipo} con {num_vertices} vértices y {num_aristas} aristas:")
    
    for u in sorted(graph.adj.keys()):
        vecinos_str = " ".join(f"({v}, {w:.1f})" for v, w in graph.adj[u])
        print(f"{u} → {vecinos_str}")