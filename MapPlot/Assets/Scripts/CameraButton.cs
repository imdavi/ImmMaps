using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class CameraButton : MonoBehaviour
{
    // Start is called before the first frame update
    private void Start()
    {   // Initializes the text component of the button
        Text txt = transform.Find("Text").GetComponent<Text>();
        txt.text = "Camera Movement: OFF";
    }

    private void Update()
    {   
        // every frame checks for an input and toggles the camera movement status
        if((Input.GetKey(KeyCode.LeftControl) || Input.GetKey(KeyCode.RightControl)) && Input.GetKey(KeyCode.M) || Input.GetKeyDown("joystick button 0"))
        {
            ButtonToggle();
        }
    }

    public void ButtonToggle()
    {   
        // Swaps active camera
        CameraControl.Toggle();
        // Changes the button text
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
