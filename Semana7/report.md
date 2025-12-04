# Reporte: Semana 7 — Árboles y Árboles Generadores Mínimos (MST)

**Autor:** Christian Gael Ortiz Ramirez 
**Asignatura:** Estructuras de Datos Avanzadas  
**Contenido:** Descripción del problema, implementación, visualizaciones y análisis.

## 1. Introduccion
Esta entrega contiene implementaciones profesionales de Prim y Kruskal para construir árboles generadores mínimos (MST). Se incluyen ejemplos, pruebas y diagramas en formato Mermaid para documentar los resultados.

## 2. Diseño y decisiones
- **Kruskal** se implementa sobre una lista de aristas ordenadas por peso y usa una estructura *Union-Find* (DSU) con compresión de caminos y unión por rango para asegurar operaciones amortizadas O(α(n)).
- **Prim** utiliza una cola de prioridad (heap) y lista de adyacencia, ideal para grafos densos o cuando se desea construir el árbol desde una raíz.
- Ambos algoritmos devuelven el conjunto de aristas del MST y su costo total. Para grafos no conexos, Kruskal devolverá un bosque generador mínimo.

## 3. Instrucciones de uso
- `mst.py` contiene la clase `GraphMST` con métodos `prim_mst()` y `kruskal_mst()`.
- Ejecutar `python3 mst.py` para ver una prueba rápida incluida.

## 4. Casos de prueba realizados
1. Triángulo simple (3 nodos) con pesos 10, 10, 15 — MST costo = 20.
2. Ejemplo en `mst.py` — ambos algoritmos deben coincidir en costo = 19.
3. Grafo no conexo — Kruskal produce un bosque (costo sumado de componentes).

## 5. Limitaciones y extensiones
- No se manejan aristas multi-grafo con identificadores únicos (dos aristas paralelas se consideran distintas).
- Extensiones sugeridas:
  - Implementar versión de Prim que recalcule con Fibonacci heap (teórico).
  - Añadir detección/filtrado de aristas duplicadas si se desea evitar paralelas exactas.

## 6. Reflexión sobre uso de IA
Parte del contenido (explicaciones y estructura del reporte) se generó y organizó con ayuda de IA. El código y las pruebas fueron verificadas y ajustadas para garantizar su funcionamiento. El estudiante debe validar y comprender cada fragmento antes de presentar el trabajo.

