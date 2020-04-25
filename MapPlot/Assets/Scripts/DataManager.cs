using System.IO;
using UnityEngine;
using System.Linq;
using System.Collections.Generic;
using System.Text;

/*
This class defines all methods to instantiate datasets and to generate the filters.
*/

class DataManager : MonoBehaviour
{
    private static Dataframe dataset;
    public static Dataframe visibleDataset;

    private static float maxFilter;
    private static float minFilter;

    private static bool newFilterApplied = false;

    /* Method: GenerateDataSetFromFile
     * Generates a float dataset from an input file.
     * The dataset is saved on the static class attribute to be used and accessed from another context.
     *
     * Parameters:
     *      - path: path to file on project structure.
     * Outputs:
     *      - N/A
     */
    public static void GenerateDataSetFromFile(string path)
    {
        // Reads lines from file
        var lines = ReadFile(path);

        var xArray = new int[lines.Length];
        var yArray = new int[lines.Length];
        var values = new float[lines.Length];

        // Iterates and separates each line
        for (int i = 0; i < lines.Length; i++)
        {
            var separatedValues = lines[i].Split(';');

            int xCoord = int.Parse(separatedValues[0]);
            int yCoord = int.Parse(separatedValues[1]);

            float.TryParse(separatedValues[2], out float value);


            xArray[i] = xCoord;
            yArray[i] = yCoord;
            values[i] = value;
        }

        dataset = new Dataframe(xArray, yArray, values);
        visibleDataset = new Dataframe(xArray, yArray, values);

        maxFilter = Mathf.CeilToInt(dataset.maxValue);
        minFilter = Mathf.FloorToInt(dataset.minValue);
    }

    /* Method: ReadFile
     * Reads all lines from file if it exists on the path.
     *
     * Parameters:
     *      - file: path to file on project structure.
     * Outputs:
     *      - array of strings containing all lines read from file.
     */
    static string[] ReadFile(string file)
    {
        if (File.Exists(file))
        {
            return File.ReadAllLines(file, Encoding.UTF8);
        }
        else
        {
            return null;
        }
    }

    public static void ResetFilters()
    {
        maxFilter = dataset.maxValue;
        minFilter = dataset.minValue;
        visibleDataset = dataset;
        newFilterApplied = true;
    }

    public static void FilterDataset()
    {
        Dataframe newDataframe = new Dataframe
        {
            width = dataset.width,
            length = dataset.length,
            depth = dataset.depth,
            minValue = dataset.minValue,
            maxValue = dataset.maxValue,
            mean = dataset.mean
        };

        float[,] newValues = new float[dataset.width, dataset.length];

        int xSize = dataset.values.GetLength(0);
        int ySize = dataset.values.GetLength(1);

        for (int i = 0; i < xSize; i++)
        {
            for (int j = 0; j < ySize; j++)
            {
                float value = dataset.values[i, j];
                bool aboveMinFilter = value > minFilter / dataset.depth;
                bool belowMaxFilter = value < maxFilter / dataset.depth;
                newValues[i, j] = (aboveMinFilter && belowMaxFilter) ? value : 0.00f;
            }
        }

        newDataframe.values = newValues;

        visibleDataset = newDataframe;
        newFilterApplied = true;
    }

    public static void SetMinFilter(float min)
    {
        minFilter = min;
    }

    public static void SetMaxFilter(float max)
    {
        maxFilter = max;
    }

    public static bool FilterApplied()
    {
        return newFilterApplied;
    }

    public static void FilteredVisualRendered()
    {
        newFilterApplied = false;
    }

    /* Method: ReadDatasetFromMessage
     * Generates a float dataset from an incoming message.
     * The dataset is saved on the static class attribute to be used and accessed from another context.
     *
     * Parameters:
     *      - message: heightmap message received via websocket.
     * Outputs:
     *      - N/A
     */
    public static void ReadDatasetFromMessage(HeightmapMessage message)
    {
        // Matrix containing the heightmap values
        var matrix = message.Heightmap;

        int matrixXlength = matrix.Length;
        int matrixYlength = matrix[0].Length;
        int matrixSize = matrixXlength * matrixYlength;

        var xArray = new int[matrixSize];
        var yArray = new int[matrixSize];
        var values = new float[matrixSize];

        int k = 0;
        // Iterates and extracts each point
        for (int i = 0; i < matrixXlength; i++)
        {
            for (int j = 0; j < matrixYlength; j++)
            {
                int xCoord = i;
                int yCoord = j;
                float value = 0.0f;

                if (matrix[i][j] is float || !float.IsNaN(matrix[i][j]))
                {
                    value = matrix[i][j];
                }

                xArray[k] = xCoord;
                yArray[k] = yCoord;
                values[k] = value;
                k += 1;
            }
        }

        dataset = new Dataframe(xArray, yArray, values);
        visibleDataset = new Dataframe(xArray, yArray, values);

        maxFilter = Mathf.CeilToInt(dataset.maxValue);
        minFilter = Mathf.FloorToInt(dataset.minValue);

        DataManager.ResetFilters();
    }
}
