using System;
using System.Collections.Generic;

namespace Semana1
{
    class Escaleras
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Problema de las Escaleras (1, 2 o 3 pasos) ===");
            
            int[] testCases = { 1, 2, 3, 4, 5, 10 };
            
            Console.WriteLine("\n--- Comparación Recursiva (Memo) vs Iterativa (Tabla) ---");
            foreach (var n in testCases)
            {
                long resRec = EscalerasMemo(n);
                long resIter = EscalerasTabla(n);
                Console.WriteLine($"n={n}: Memo={resRec}, Tabla={resIter} - {(resRec == resIter ? "OK" : "ERROR")}");
            }
        }

        // Diccionario para memoización
        static Dictionary<int, long> memo = new Dictionary<int, long>();

        static long EscalerasMemo(int n)
        {
            // Casos base
            if (n < 0) return 0;
            if (n == 0) return 1; // Una forma de "no subir nada" (estar en la base) o llegar a la meta exacta
            
            // Verificación de memoización
            if (memo.ContainsKey(n)) return memo[n];
            
            // Recurrencia: f(n) = f(n-1) + f(n-2) + f(n-3)
            long resultado = EscalerasMemo(n - 1) + EscalerasMemo(n - 2) + EscalerasMemo(n - 3);
            
            memo[n] = resultado;
            return resultado;
        }

        static long EscalerasTabla(int n)
        {
            if (n < 0) return 0;
            if (n == 0) return 1;
            
            // Crear tabla dp
            // dp[i] almacena el número de formas de llegar al escalón i
            long[] dp = new long[n + 1];
            
            // Casos base iniciales
            dp[0] = 1; // Base
            
            // Llenar tabla
            for (int i = 1; i <= n; i++)
            {
                // Sumar formas desde los escalones anteriores posibles
                if (i - 1 >= 0) dp[i] += dp[i - 1];
                if (i - 2 >= 0) dp[i] += dp[i - 2];
                if (i - 3 >= 0) dp[i] += dp[i - 3];
            }
            
            return dp[n];
        }
    }
}
