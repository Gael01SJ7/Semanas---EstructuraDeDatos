# Actividades con IA - Respuestas

## Actividad 1: 5 escenarios y recomendación de algoritmo
Escenario | Algoritmo recomendado | Justificación | Estructuras de datos | Escalabilidad
---|---|---|---|---
Red de fibra entre ciudades | Kruskal | Entrada natural: lista de aristas entre ciudades (dispersa) y se desea minimizar costo total | Lista de aristas, DSU | Si crece 10x, ordenar E crece ~10x log(10x), DSU sigue siendo eficiente
Red de campus (muchas conexiones posibles) | Prim | Puede partir de un nodo, lista de adyacencia y heap funcionan bien en grafos densos | Lista de adyacencia + heap | Con 10x nodos, E crece más rápido; Prim con heap mantiene O(E log V)
Clustering de puntos geográficos | Kruskal | Facilita eliminar aristas más caras para separar clústeres | Lista de aristas ordenada | Crece bien; usar estructuras externas si E demasiado grande
Diseño de red eléctrica urbana | Prim | Si se modela por adyacencia local y se quiere construir desde subestación, Prim es natural | Lista de adyacencia + heap | Escala similar a caso campus
TSP aproximado (Paso en Christofides) | Kruskal (como paso) | MST se usa como cota inferior y base para construir soluciones aproximadas | Lista de aristas + DSU | 10x nodos aumenta coste computacional de manera significativa; usar heurísticas y reducción de aristas

## Actividad 2: Depuración guía (resumen)
- Si tu Kruskal devuelve un costo mayor al esperado, revisa:
  1. Si la lista de aristas se está ordenando por peso (clave 2).
  2. Si `union` devuelve True solo cuando une componentes distintas.
  3. Si la estructura DSU fue reinicializada entre ejecuciones.
- Casos de prueba sugeridos:
  * Triángulo con pesos 10,10,15 (esperado 20).
  * Grafo con aristas paralelas iguales (comprobar no duplicar).
  * Grafo desconexo (esperar bosque y verificar número de aristas).

## Actividad 3: Mermaid + explicación
- Archivo `diagram_mermaid.mmd` incluido en la carpeta.
- Convenciones sugeridas:
  * Nodos del MST: color verde.
  * Aristas del MST: borde más grueso y color verde.
  * Aristas descartadas: color gris claro.
- Texto explicativo (breve):
  > El diagrama muestra el grafo original con todas las aristas etiquetadas por su peso. Las aristas seleccionadas por el MST están resaltadas (verde y borde más grueso). El MST conecta todos los nodos con el costo mínimo total posible, sin crear ciclos.