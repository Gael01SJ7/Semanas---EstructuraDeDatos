# Reporte Semana 1: Recursividad y Programación Dinámica

## Actividad 1: Torres de Hanoi

### Comparación: Recursividad vs Iteración

En esta actividad implementamos dos soluciones para el clásico problema de las Torres de Hanoi: una recursiva y una iterativa.

#### Solución Recursiva
La solución recursiva es elegante y directa. Se basa en la definición inductiva del problema:
1. Mover `n-1` discos de Origen a Auxiliar.
2. Mover el disco `n` de Origen a Destino.
3. Mover `n-1` discos de Auxiliar a Destino.

**Código:**
```csharp
void Solve(int k, char from, char to, char aux)
{
    if (k == 0) return;
    Solve(k - 1, from, aux, to);
    moves.Add($"{from} -> {to}");
    Solve(k - 1, aux, to, from);
}
```

#### Solución Iterativa
La solución iterativa es significativamente más compleja de implementar. Requiere simular la pila de recursión o utilizar propiedades matemáticas del problema (como el movimiento cíclico de los discos dependiendo de la paridad de `n`).
Nuestra implementación utiliza el enfoque matemático:
- Los movimientos impares siempre mueven el disco más pequeño.
- Los movimientos pares mueven el único disco legal que no es el más pequeño.

#### Resultados del Benchmark
Al ejecutar el análisis comparativo, observamos que ambas soluciones generan la misma secuencia de movimientos (corrección verificada).
En términos de tiempo de ejecución (Ticks):
- Para `n` pequeños, la diferencia es despreciable.
- La versión recursiva tiene una sobrecarga por las llamadas a función (stack overhead), pero la lógica es muy simple.
- La versión iterativa evita el stack overhead pero tiene una lógica de control más pesada por iteración.

## Actividad 2: Puente a DP (Escaleras)

### El Problema
El problema consiste en encontrar de cuántas formas se puede subir una escalera de `n` peldaños si podemos subir 1, 2 o 3 peldaños a la vez.

### Análisis de la Recurrencia
Para llegar al escalón `n`, pudimos haber venido de:
- El escalón `n-1` (dando 1 paso).
- El escalón `n-2` (dando 2 pasos).
- El escalón `n-3` (dando 3 pasos).

Por lo tanto, la relación de recurrencia es:
`f(n) = f(n-1) + f(n-2) + f(n-3)`

### Implementación
Se implementaron dos versiones:
1. **Recursiva con Memoización (Top-Down):** Utiliza un diccionario para guardar los resultados de `f(n)` ya calculados y evitar re-trabajo.
2. **Iterativa (Bottom-Up):** Utiliza un arreglo `dp[]` donde `dp[i]` almacena las formas de llegar al escalón `i`, llenando la tabla desde `i=1` hasta `n`.

**Código Clave (Iterativo):**
```csharp
for (int i = 1; i <= n; i++)
{
    if (i - 1 >= 0) dp[i] += dp[i - 1];
    if (i - 2 >= 0) dp[i] += dp[i - 2];
    if (i - 3 >= 0) dp[i] += dp[i - 3];
}
```

Ambas versiones producen el mismo resultado, pero la versión iterativa es más eficiente en espacio (evita la recursión profunda) y tiempo (evita el overhead de llamadas y búsquedas en diccionario).
