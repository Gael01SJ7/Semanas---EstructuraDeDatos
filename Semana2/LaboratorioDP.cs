using System;
using System.Collections.Generic;

namespace Semana2
{
    class LaboratorioDP
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Laboratorio de Consolidación DP ===");

            // Ejercicio 1: Análisis (Solo comentarios en código, pero imprimimos algo)
            Console.WriteLine("\n--- Ejercicio 1: Análisis ---");
            Console.WriteLine("Ver código fuente para análisis de Tribonacci, Suma y Factorial.");

            // Ejercicio 2: Formas de sumar n
            Console.WriteLine("\n--- Ejercicio 2: Formas de sumar n (1 o 2) ---");
            int n = 5;
            Console.WriteLine($"Formas({n}) Ingenuo: {FormasIngenuo(n)}");
            Console.WriteLine($"Formas({n}) Memo:    {FormasMemo(n)}");
            Console.WriteLine($"Formas({n}) Tabla:   {FormasTabla(n)}");

            // Ejercicio 3: Cambio de Monedas
            Console.WriteLine("\n--- Ejercicio 3: Cambio de Monedas [1, 3, 4] ---");
            int amount = 6;
            int coins = MinMonedas(amount, new int[] { 1, 3, 4 });
            Console.WriteLine($"Mínimo monedas para {amount}: {coins}");

            // Ejercicio 4: Debugging
            Console.WriteLine("\n--- Ejercicio 4: Fibonacci Corregido ---");
            Console.WriteLine($"Fibonacci(5): {FibonacciCorregido(5)}");
        }

        /*
         * EJERCICIO 1: ANÁLISIS
         * 
         * A. Tribonacci: f(n) = f(n-1) + f(n-2) + f(n-3)
         *    - Tiene subproblemas repetidos.
         *    - Se beneficia de DP.
         *    
         * B. Suma Acumulativa: f(n) = f(n-1) + n
         *    - NO tiene subproblemas repetidos (estructura lineal).
         *    - No necesita DP (es O(n) recursivo o O(1) con fórmula).
         *    
         * C. Factorial: f(n) = n * f(n-1)
         *    - NO tiene subproblemas repetidos.
         *    - No necesita DP.
         */

        // EJERCICIO 2: Formas de sumar n (pasos 1, 2)
        
        static int FormasIngenuo(int n)
        {
            if (n <= 0) return 1; // Asumimos 1 forma para 0 (no hacer nada) o negativos como base
            if (n == 1) return 1;
            return FormasIngenuo(n - 1) + FormasIngenuo(n - 2);
        }

        static Dictionary<int, int> memoFormas = new Dictionary<int, int>();
        static int FormasMemo(int n)
        {
            if (n <= 0) return 1;
            if (n == 1) return 1;
            
            if (memoFormas.ContainsKey(n)) return memoFormas[n];
            
            int res = FormasMemo(n - 1) + FormasMemo(n - 2);
            memoFormas[n] = res;
            return res;
        }

        static int FormasTabla(int n)
        {
            if (n <= 1) return 1;
            
            int[] dp = new int[n + 1];
            dp[0] = 1;
            dp[1] = 1;
            
            for (int i = 2; i <= n; i++)
            {
                dp[i] = dp[i - 1] + dp[i - 2];
            }
            return dp[n];
        }

        // EJERCICIO 3: Cambio de Monedas
        static int MinMonedas(int n, int[] monedas)
        {
            if (n == 0) return 0;
            if (n < 0) return int.MaxValue;

            int[] dp = new int[n + 1];
            Array.Fill(dp, int.MaxValue - 1); // Evitar overflow al sumar 1
            dp[0] = 0;

            for (int i = 1; i <= n; i++)
            {
                foreach (var moneda in monedas)
                {
                    if (i >= moneda)
                    {
                        dp[i] = Math.Min(dp[i], 1 + dp[i - moneda]);
                    }
                }
            }

            return dp[n] > n ? -1 : dp[n];
        }

        // EJERCICIO 4: Fibonacci Corregido
        static int FibonacciCorregido(int n)
        {
            if (n <= 0) return 0;
            if (n == 1) return 1;

            // Error 1: Tamaño array debe ser n + 1 para acceder a índice n
            int[] dp = new int[n + 1];
            
            dp[0] = 0; // Caso base implícito o explícito
            dp[1] = 1;

            // Error 2: Rango debe incluir n
            for (int i = 2; i <= n; i++)
            {
                dp[i] = dp[i - 1] + dp[i - 2];
            }

            // Error 3: Ahora es seguro acceder a dp[n]
            return dp[n];
        }
    }
}
