using System.Linq;
using UnityEngine;

class Dataframe
{
    public int width;
    public int length;
    public int depth;
    public float[,] values;

    public Dataframe(int[] x, int[] y, float[] v)
    {
        width = x.Max()+1;
        length = y.Max()+1;
        depth = Mathf.CeilToInt(v.Max());

        values = new float[width, length];

        for (int i = 0; i < x.Length; i++)
        { 
            values[x[i], y[i]] = v[i]/depth;
        }
    }

    void RescaleValues(float scale)
    {
        int xSize = values.GetLength(0);
        int ySize = values.GetLength(1);
        
        for(int i = 0; i < xSize; i++)
        {
            for(int j = 0; j < ySize; j++)
            {
                values[i, j] *= scale;
            }
        }

    }
}