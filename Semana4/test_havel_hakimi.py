# Actividad IA #1 – Generación de Casos de Prueba Exhaustivos
# Materia: Estructuras de Datos
# Semana 4

from Grafo import is_graphical_sequence

print("=== Pruebas de Havel-Hakimi - Semana 4 ===\n")

# 10 CASOS DE PRUEBA (5 válidos + 5 inválidos)
test_cases = [
    ([3, 2, 2, 1], "✓ Gráfica"),
    ([4, 3, 3, 2, 2, 2], "✓ Gráfica"),
    ([4, 3, 3, 2, 2, 2, 1, 1], "✓ Gráfica"),
    ([5, 5, 4, 4, 3, 3, 2, 2, 1, 1], "✓ Gráfica"),
    ([6, 6, 5, 5, 5, 4, 4, 3, 3, 3, 2, 2, 1, 1, 1], "✓ Gráfica"),
    ([3, 3, 3, 1], "✖ No Gráfica"),
    ([5, 3, 2, 2, 1], "✖ No Gráfica"),
    ([8, 2, 2, 2, 2, 2, 2, 2], "✖ No Gráfica"),
    ([4, 4, 4, 1, 0, 0, 0], "✖ No Gráfica"),
    ([6, 1, 1, 1, 1, 1, 1], "✖ No Gráfica"),
]

# 🔹 EJECUCIÓN DE LAS PRUEBAS
for i, (seq, expected) in enumerate(test_cases, start=1):
    result = is_graphical_sequence(seq)
    status = "✓ Gráfica" if result else "✖ No Gráfica"
    print(f"{i}. {seq} → {status} (Esperado: {expected})")

print("\n= Fin de pruebas =")


