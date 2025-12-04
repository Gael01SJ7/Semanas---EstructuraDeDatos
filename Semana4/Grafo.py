# grafo.py
# Algoritmo de Havel-Hakimi para verificar si una secuencia es gráfica

def is_graphical_sequence(degrees):
    if not degrees:
        return True

    seq = sorted(degrees, reverse=True)

    if sum(seq) % 2 != 0 or seq[0] >= len(seq):
        return False

    while seq:
        d1 = seq.pop(0)

        if d1 == 0:
            return True
        if d1 > len(seq):
            return False

        for i in range(d1):
            seq[i] -= 1
            if seq[i] < 0:
                return False

        seq.sort(reverse=True)

    return True



# Pruebas y predicciones
if __name__ == "__main__":
     # Pruebas básicas
    secuencia1 = [4, 3, 3, 2, 2, 2, 1, 1]
    secuencia2 = [3, 3, 3, 1]

    print("Secuencia 1:", secuencia1, "→", is_graphical_sequence(secuencia1))
    print("Secuencia 2:", secuencia2, "→", is_graphical_sequence(secuencia2))

   
    # Actividad IA #1 – Verificación de predicciones manuales
    print("3 Prediciones - Actividad IA #1 - Verificaciones de prediciones")
    predicciones = {
        1: ([4, 3, 3, 2, 2, 1, 1], True),   # True = GRÁFICA
        2: ([3, 3, 3, 1, 1, 1], False),
        3: ([0, 0, 0, 0], True)
    }

    print("\n=== Verificación de predicciones manuales ===")
    for num, (seq, prediccion) in predicciones.items():
        resultado = is_graphical_sequence(seq.copy())
        acierto = "✅" if resultado == prediccion else "❌"
        print(f"Caso {num}: Predicción = {'GRÁFICA' if prediccion else 'NO GRÁFICA'}, "
              f"Resultado real = {'GRÁFICA' if resultado else 'NO GRÁFICA'} → {acierto}")