using System.IO;
using UnityEngine;

class DataManager
{
    public static Dataframe dataset;

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
        for (int i=0; i < lines.Length; i++)
        {
            var separatedValues = lines[i].Split(';');

            int xCoord = int.Parse(separatedValues[0]);
            int yCoord = int.Parse(separatedValues[1]);
            float value = float.Parse(separatedValues[2]);

            xArray[i] = xCoord;
            yArray[i] = yCoord;
            values[i] = value;
        }

        dataset = new Dataframe(xArray, yArray, values);
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
            return File.ReadAllLines(file);
        }
        else
        {
            return null;
        }
    }

}