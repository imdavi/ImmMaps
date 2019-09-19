using UnityEngine;

public class MainClass : MonoBehaviour
{
    void Start()
    {
        DataManager.GenerateDataSetFromFile("Assets/input/_input.csv");
    }
}