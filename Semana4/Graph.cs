using System;
using System.Collections.Generic;
using System.Linq;

namespace Semana4
{
    public class Graph
    {
        public static bool IsGraphicalSequence(List<int> degrees)
        {
            if (degrees.Count == 0) return true;

            var seq = new List<int>(degrees);
            seq.Sort((a, b) => b.CompareTo(a));

            int sum = seq.Sum();
            if (sum % 2 != 0 || seq[0] >= seq.Count) return false;

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
}
