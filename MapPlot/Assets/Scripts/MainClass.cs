using UnityEngine;

public class MainClass : MonoBehaviour
{

    public Camera mainCamera;
    public Camera mobileCam;

    void Start()
    {
        //string filepath = "Assets/input/map_input.csv";
        string filepath = Application.dataPath + "/input/map_input.csv";
        // Initializes the dataset from a file on the application default path
        DataManager.GenerateDataSetFromFile(filepath);
        // Sets the status of the cameras.
        mainCamera.enabled = true;
        mobileCam.enabled = false;
    }

    private void Update()
    {
        // Updates the camera status
        mainCamera.enabled = !CameraControl.GetCameraMovementStatus();
        mobileCam.enabled = CameraControl.GetCameraMovementStatus();
    }
}