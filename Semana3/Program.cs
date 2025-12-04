using System;
using System.IO;
using System.Linq;

class Program
{
    static void Main()
    {
        Console.WriteLine("=== MAPA DE CIUDAD - Red de Transporte ===\n");

        var ciudad = new Graph<string>(directed: true);

        // === LEER ARISTAS DESDE EL ARCHIVO ===
        string archivo = "edges_directed.txt";

        if (File.Exists(archivo))
        {
            string[] lineas = File.ReadAllLines(archivo);

            foreach (var linea in lineas)
            {
                if (string.IsNullOrWhiteSpace(linea)) continue;
                var partes = linea.Split(' ', StringSplitOptions.RemoveEmptyEntries);
                if (partes.Length < 3) continue;

                string origen = partes[0];
                string destino = partes[1];
                try
                {
                    double peso = double.Parse(partes[2]);
                    ciudad.AddEdge(origen, destino, peso);
                }
                catch (FormatException)
                {
                    Console.WriteLine($"⚠️  Error de formato en la línea: '{linea}'. Se omitirá.");
                }
            }

            Console.WriteLine($"Archivo '{archivo}' cargado exitosamente ✅\n");
        }
        else
        {
            Console.WriteLine($"⚠️ No se encontró el archivo '{archivo}', usando valores por defecto.\n");

            // Si no existe el archivo, usa datos por defecto
            // (Estos datos coinciden con el archivo ciudad.txt de la implementación de Python)
            ciudad.AddEdge("A", "G", 1.0);
            ciudad.AddEdge("B", "H", 3.0);
            ciudad.AddEdge("C", "D", 2.0);
            ciudad.AddEdge("A", "B", 2);
            ciudad.AddEdge("B", "A", 2);
            ciudad.AddEdge("A", "C", 3);
            ciudad.AddEdge("C", "A", 3);
            ciudad.AddEdge("A", "G", 1);
            ciudad.AddEdge("B", "D", 1);
            ciudad.AddEdge("C", "E", 4);
            ciudad.AddEdge("E", "C", 4);
            ciudad.AddEdge("D", "B", 1);
            ciudad.AddEdge("D", "F", 5);
            ciudad.AddEdge("F", "D", 5);
            ciudad.AddEdge("E", "F", 2);
            ciudad.AddEdge("F", "E", 2);
            ciudad.AddEdge("G", "H", 6);
            ciudad.AddEdge("H", "G", 6);
            ciudad.AddEdge("F", "E", 4);
            ciudad.AddEdge("H", "A", 5);
        }

        // Mostrar conexiones
        ciudad.Print();

        Console.WriteLine("\n=== ANÁLISIS: Conexión E-F (Multigrafo) ===\n");
        Console.WriteLine($"E→F existe? {ciudad.HasEdge("E", "F")}");
        Console.WriteLine($"F→E existe? {ciudad.HasEdge("F", "E")}\n");

        var rutasFE = ciudad.GetEdgeWeights("F", "E");
        Console.WriteLine($"Rutas disponibles F→E: {rutasFE.Count}");
        foreach (var peso in rutasFE)
            Console.WriteLine($"  • Ruta con distancia: {peso} km");

        Console.WriteLine("\n📚 Concepto de MULTIGRAFO:");
        Console.WriteLine("   - Permite múltiples aristas entre los mismos vértices.");
        Console.WriteLine("   - Ejemplo práctico: rutas alternas con diferente distancia o costo.\n");

        Console.WriteLine("=== CONSULTAS GENERALES ===\n");
        Console.WriteLine($"¿Puedo ir de A al Hospital (G)? {ciudad.HasEdge("A", "G")}");
        Console.WriteLine($"¿Puedo volver de G a A? {ciudad.HasEdge("G", "A")}\n");

        Console.WriteLine($"¿Existe F→E con 2.0 km? {ciudad.HasEdgeWithWeight("F", "E", 2.0)}");
        Console.WriteLine($"¿Existe F→E con 4.0 km? {ciudad.HasEdgeWithWeight("F", "E", 4.0)}\n");

        Console.WriteLine("=== ANÁLISIS DE GRADOS ===\n");
        var zonas = new[] { "A", "B", "C", "D", "E", "F", "G", "H" };
        foreach (var z in zonas.OrderBy(z => z))
            Console.WriteLine($"Zona {z}: salida={ciudad.OutDegree(z)}, entrada={ciudad.InDegree(z)}");

        Console.WriteLine("\n=== DESTINOS DESDE CENTRO COMERCIAL (A) ===\n");
        foreach (var (destino, dist) in ciudad.Neighbors("A"))
            Console.WriteLine($"  → Zona {destino} a {dist} km");

        Console.WriteLine("\n======================================================================");
        Console.WriteLine("PRUEBA: Cierre temporal de calle por mantenimiento");
        Console.WriteLine("======================================================================\n");

        Console.WriteLine("Cerrando calle C→D...");
        var removed = ciudad.RemoveEdge("C", "D");
        Console.WriteLine($"Resultado: {(removed > 0 ? "✓ Eliminada" : "✗ No existía")}\n");
        Console.WriteLine($"C→D: {(ciudad.HasEdge("C", "D") ? "Existe" : "CERRADA")}");
        Console.WriteLine($"D→C: {(ciudad.HasEdge("D", "C") ? "Existe" : "Cerrada")}\n");

        // Guardar resultados en TXT
        string salida = "resultado.txt";
        File.WriteAllText(salida, $"Análisis completado correctamente.\nMultigrafo cargado desde '{archivo}'");
        Console.WriteLine($"Archivo '{salida}' generado exitosamente ✅\n");

        Console.WriteLine("✓ Análisis completado.");
    }
}
