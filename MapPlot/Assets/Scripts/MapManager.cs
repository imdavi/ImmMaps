using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MapManager : MonoBehaviour
{

    int width = 100;
    int length = 100;
    int depth = 20;

    float scale = 20f;

    // Start is called before the first frame update
    void Start()
    {
        Terrain map = GetComponent<Terrain>();
        map.terrainData = UpdateTerrainData(map.terrainData, DataManager.visibleDataset);
    }

    private void Update()
    {
        if (DataManager.FilterApplied())
        {
            Terrain map = GetComponent<Terrain>();
            map.terrainData = UpdateTerrainData(map.terrainData, DataManager.visibleDataset);
            DataManager.FilteredVisualRendered();
        }
    }

    private TerrainData UpdateTerrainData(TerrainData td, Dataframe ds = null)
    {
        float[,] heights;
        if (ds != null)
        {
            // Debug.Log("Input generated map");
            width = ds.width;
            length = ds.length;
            depth = ds.depth;
            heights = ds.values;
        }
        else
        {
            heights = GenerateHeights();
            // Debug.Log("Noise generated map");
        }
        
        td.size = new Vector3(width, depth, length);
        td.heightmapResolution = width + 1;
        td.SetHeights(0, 0, heights);
        return td;
    }

    private float[,] GenerateHeights()
    {
        float[,] heights = new float[width, length];
        for (int x=0; x<width; x++)
        {
            for(int y=0; y < length; y++)
            {
                heights[x, y] = GetValue(x, y);
            }
        }

        return heights;
    }

    private float GetValue(int x, int y)
    {
        float xCoord = (float)x / width * scale;
        float yCoord = (float)y / length * scale;

        return Mathf.PerlinNoise(xCoord, yCoord);
    }

}
