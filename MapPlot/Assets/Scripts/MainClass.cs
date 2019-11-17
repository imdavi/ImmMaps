using UnityEngine;

public class MainClass : MonoBehaviour
{

    public Camera mainCamera;
    public Camera mobileCam;

    void Start()
    {
        Debug.Log("Loading dataset");
        //DataManager.GenerateDataSetFromFile(Application.dataPath+"/input/_input.csv");
        mainCamera.enabled = true;
        mobileCam.enabled = false;
    }

    private void Update()
    {
        mainCamera.enabled = !CameraControl.GetCameraMovementStatus();
        mobileCam.enabled = CameraControl.GetCameraMovementStatus();
    }
}