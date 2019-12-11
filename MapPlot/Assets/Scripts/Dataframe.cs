using System.Linq;
using UnityEngine;

/*
This class defines a data structure to hold the values of the array.
Also holds a few parameters obtained from the array as the width, length etc.
*/

class Dataframe
{
    public int width;
    public int length;
    public int depth;
    public float[,] values;
    public float maxValue;
    public float minValue;
    public float mean;

    public Dataframe()
    {
    }

    public Dataframe(int[] x, int[] y, float[] v)
    {
        // Initializes a dataframe populating all parameters.
        width = x.Max()+1;
        length = y.Max()+1;
        depth = Mathf.CeilToInt(v.Max());

        mean = v.Average();
        maxValue = v.Max();
        minValue = v.Min();

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