using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class CameraButton : MonoBehaviour
{
    // Start is called before the first frame update
    private void Start()
    {
        Text txt = transform.Find("Text").GetComponent<Text>();
        txt.text = "Camera Movement: OFF";
    }

    private void Update()
    {
        if((Input.GetKey(KeyCode.LeftControl) || Input.GetKey(KeyCode.RightControl)) && Input.GetKey(KeyCode.M))
        {
            ButtonToggle();
        }
    }

    public void ButtonToggle()
    {
        CameraControl.Toggle();

        Text txt = transform.Find("Text").GetComponent<Text>();
        if (CameraControl.GetCameraMovementStatus())
        {
            txt.text = "Camera Movement: ON";
        }
        else
        {
            txt.text = "Camera Movement: OFF";
        }
    }

}
