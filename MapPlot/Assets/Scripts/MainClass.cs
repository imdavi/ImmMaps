using UnityEngine;

public class MainClass : MonoBehaviour
{

    public Camera mainCamera;
    public Camera mobileCam;

    void Start()
    {
        //string filepath = "Assets/input/map_input.csv";
        string filepath = Application.dataPath + "/input/map_input.csv";
        DataManager.GenerateDataSetFromFile(filepath);
        mainCamera.enabled = true;
        mobileCam.enabled = false;
    }

    private void Update()
    {
        mainCamera.enabled = !CameraControl.GetCameraMovementStatus();
        mobileCam.enabled = CameraControl.GetCameraMovementStatus();
    }
}