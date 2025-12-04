using System;
using System.Collections.Generic;

namespace Semana2
{
    class MiniProyecto
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Mini-Proyecto: Suma Máxima Sin Adyacentes (House Robber) ===");
            
            int[] casas1 = { 1, 2, 3, 1 };
            int[] casas2 = { 2, 7, 9, 3, 1 };
            
            Console.WriteLine($"Casas 1 [{string.Join(",", casas1)}]: Max Robo = {Robar(casas1)}"); // Esperado: 4 (1+3)
            Console.WriteLine($"Casas 2 [{string.Join(",", casas2)}]: Max Robo = {Robar(casas2)}"); // Esperado: 12 (2+9+1)
        }

        static int Robar(int[] nums)
        {
            if (nums == null || nums.Length == 0) return 0;
            if (nums.Length == 1) return nums[0];
            
            // dp[i] = máximo dinero robando hasta la casa i
            int[] dp = new int[nums.Length];
            
            // Casos base
            dp[0] = nums[0];
            dp[1] = Math.Max(nums[0], nums[1]);
            
            for (int i = 2; i < nums.Length; i++)
            {
                // Decisión: 
                // 1. No robar casa i -> me quedo con lo de i-1
                // 2. Robar casa i -> sumo valor i + lo de i-2
                dp[i] = Math.Max(dp[i - 1], nums[i] + dp[i - 2]);
            }
            
            return dp[nums.Length - 1];
        }
    }
}
