
"""
Mapa de ciudad - Análisis de red de transporte urbano.
Ejemplo educativo sobre grafos mixtos (dirigidos + no dirigidos).
"""

from grafo import *

def main():
    print("=" * 70)
    print("MAPA DE CIUDAD - Red de Transporte Urbano")
    print("=" * 70)
    
    # Diccionario de descripciones de zonas
    zonas_desc = {
        "A": "Centro Comercial",
        "B": "Zona Norte",
        "C": "Zona Sur",
        "D": "Este Industrial",
        "E": "Oeste Residencial",
        "F": "Zona Industrial",
        "G": "Hospital",
        "H": "Estadio"
    }
    
    # Cargar grafo desde archivo
    try:
        ciudad = load_graph("ciudad.txt", directed=True)
        print("\n✓ Grafo cargado exitosamente desde 'ciudad.txt'\n")
    except FileNotFoundError as e:
        print(f"\n✗ Error: {e}")
        print("   Asegúrate de tener el archivo 'ciudad.txt' en el directorio actual.")
        return
    
    # Imprimir el grafo completo
    print_graph(ciudad)
    
    # === ANÁLISIS ESPECIAL: Problema E-F ===
    print("\n" + "=" * 70)
    print("ANÁLISIS ESPECIAL: Conexión E-F (Multigrafo)")
    print("=" * 70)
    
    print("\n Observación importante:")
    print("   Hay MÚLTIPLES rutas entre E (Oeste Residencial) y F (Zona Industrial)\n")
    
    # Obtener todas las rutas E→F
    rutas_e_f = get_edge_weights(ciudad, "E", "F")
    print(f"Rutas desde E→F: {len(rutas_e_f)} ruta(s)")
    for i, peso in enumerate(rutas_e_f, 1):
        print(f"  {i}. Distancia: {peso:.1f} km")
    
    # Obtener todas las rutas F→E
    rutas_f_e = get_edge_weights(ciudad, "F", "E")
    print(f"\nRutas desde F→E: {len(rutas_f_e)} ruta(s)")
    for i, peso in enumerate(rutas_f_e, 1):
        print(f"  {i}. Distancia: {peso:.1f} km")
    
    if len(rutas_f_e) > 1:
        print("\n⚠️  MÚLTIPLES RUTAS DETECTADAS (Multigrafo):")
        print("   📚 Concepto: Esto es un MULTIGRAFO ponderado.")
        print("       Permite múltiples aristas entre el mismo par de vértices.")
        print("\n   🚗 Interpretación práctica:")
        print(f"       - Ruta 1 ({rutas_f_e[0]:.1f} km): Carretera local bidireccional")
        print(f"       - Ruta 2 ({rutas_f_e[1]:.1f} km): Autopista de cuota (más larga pero quizá más rápida)")
    
    # === CONSULTAS GENERALES ===
    print("\n" + "=" * 70)
    print("CONSULTAS DE CONECTIVIDAD")
    print("=" * 70 + "\n")
    
    consultas = [
        ("A", "G", "¿Puedo ir del Centro al Hospital?"),
        ("G", "A", "¿Puedo volver del Hospital al Centro?"),
        ("E", "F", "¿Existe E→F?"),
        ("F", "E", "¿Existe F→E?"),
        ("B", "H", "¿Puedo ir de Zona Norte al Estadio?"),
        ("H", "B", "¿Puedo volver del Estadio a Zona Norte?"),
    ]
    
    for origen, destino, pregunta in consultas:
        existe = has_edge(ciudad, origen, destino)
        simbolo = "✓" if existe else "✗"
        print(f"{simbolo} {pregunta}")
        print(f"   {origen}→{destino}: {'SÍ' if existe else 'NO'}\n")
    
    # Verificar aristas específicas por peso
    print("Verificación de aristas específicas por peso:")
    print(f"  ¿Existe F→E con 2.0 km? {has_edge_with_weight(ciudad, 'F', 'E', 2.0)}")
    print(f"  ¿Existe F→E con 4.0 km? {has_edge_with_weight(ciudad, 'F', 'E', 4.0)}\n")
    
    # === ANÁLISIS DE GRADOS ===
    print("=" * 70)
    print("ANÁLISIS DE GRADOS (Conectividad)")
    print("=" * 70 + "\n")
    
    for zona in sorted(ciudad.adj.keys()):
        desc = zonas_desc.get(zona, "Desconocida")
        out_deg = out_degree(ciudad, zona)
        in_deg = in_degree(ciudad, zona)
        
        print(f"Zona {zona} ({desc}):")
        print(f"  ├─ Grado salida:  {out_deg} (calles que salen)")
        print(f"  └─ Grado entrada: {in_deg} (calles que llegan)")
        
        if out_deg == 0:
            print(f"     ⚠️  Zona sin salidas!")
        if in_deg == 0:
            print(f"     ⚠️  Zona inaccesible!")
        print()
    
    # === RUTAS DESDE CENTRO COMERCIAL ===
    print("=" * 70)
    print("RUTAS DIRECTAS DESDE CENTRO COMERCIAL (A)")
    print("=" * 70 + "\n")
    
    try:
        for destino, distancia in neighbors(ciudad, "A"):
            desc_destino = zonas_desc.get(destino, "Desconocida")
            print(f"  → Zona {destino} ({desc_destino}) a {distancia:.1f} km")
    except KeyError:
        print("  ✗ No se encontró la zona A")
    
    # === PRUEBA DE ELIMINACIÓN ===
    print("\n" + "=" * 70)
    print("PRUEBA: Cierre temporal de calle por mantenimiento")
    print("=" * 70 + "\n")
    
    print("Cerrando calle C→D (Zona Sur → Este Industrial)...")
    removed_count = remove_edge(ciudad, "C", "D")
    print(f"Resultado: {'✓ Eliminada' if removed_count > 0 else '✗ No existía'} ({removed_count} arista(s) quitada(s))\n")
    
    print("Estado de la red después del cierre:")
    print(f"  C→D: {'Existe' if has_edge(ciudad, 'C', 'D') else 'CERRADA'}")
    print(f"  D→C: {'Existe' if has_edge(ciudad, 'D', 'C') else 'Cerrada'} (bidireccional no afectada)")
    
    print("\n✓ Análisis completado.")

if __name__ == "__main__":
    main()