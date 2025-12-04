using System;
using System.Collections.Generic;
using System.Linq;

public static class GraphValidator
{
    // <summary>
    //Valida si una secuencia es gráfica usando Havel-Hakimi.
    // Complejidad: O(n² log n)
    //</summary>
    public static bool IsGraphicalSequence(List<int> degrees)
    {
        if (degrees.Count == 0) return true;

        // Copiar y ordenar
        var seq = new List<int>(degrees);

        // Verificar suma par y grado máximo
        int sum = seq.Sum();
        if (sum % 2 != 0 || seq[0] >= seq.Count) return false;

        // Aplicar Havel-Hakimi
        while (seq.Count > 0)
        {
            int d1 = seq[0];
            seq.RemoveAt(0);

            if (d1 == 0) return true;
            if (d1 > seq.Count) return false;

            for (int i = 0; i < d1; i++)
            {
                seq[i]--;
                if (seq[i] < 0) return false;
            }

            seq.Sort((a, b) => b.CompareTo(a));
        }

        return true;
    }
}

class Program
{
     static void Main(string[] args)
    {
        List<List<int>> testCases = new List<List<int>>
        {
            new List<int> {4, 3, 3, 2, 2, 2, 1, 1},
            new List<int> {3, 2, 2, 1},
            new List<int> {4, 3, 3, 2, 2, 2},
            new List<int> {0, 0, 0, 0},
            new List<int> {3, 3, 3, 3},
            new List<int> {3, 3, 3, 1},
            new List<int> {5, 5, 4, 3, 2, 1},
            new List<int> {3, 2, 1},
            new List<int> {6, 1, 1, 1, 1, 1, 1},
            new List<int> {5, 3, 2, 2, 1}
        };

        Console.WriteLine("== Pruebas oficiales de Havel–Hakimi ===\n");
        foreach (var testCase in testCases)
        {
            bool resultado = GraphValidator.IsGraphicalSequence(testCase);
            string estado = resultado ? "✓ Gráfica" : "✖ No Gráfica";
            Console.WriteLine($"Secuencia: [{string.Join(", ", testCase)}] -> {estado}");
        }
    }
}