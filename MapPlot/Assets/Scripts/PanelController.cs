using UnityEngine;
using UnityEngine.UI;

/*
Starts the text labels on the Panel.
*/

public class PanelController : MonoBehaviour
{
    public Text maxValue;
    public Text minValue;
    public Text meanValue;

    private bool firstLoad = true;

    private void Update()
    {
        if (DataManager.visibleDataset == null)
        {
            return;
        }
        if (firstLoad)
        {
            firstLoad = false;
            maxValue.text = DataManager.visibleDataset.maxValue.ToString(format: "n2");
            minValue.text = DataManager.visibleDataset.minValue.ToString(format: "n2");
            meanValue.text = DataManager.visibleDataset.mean.ToString(format: "n2");
        }

    }
}
