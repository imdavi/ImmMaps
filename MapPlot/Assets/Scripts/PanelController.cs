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

    // Start is called before the first frame update
    void Start()
    {
        if (DataManager.visibleDataset == null)
        {
            return;
        }
        maxValue.text = DataManager.visibleDataset.maxValue.ToString(format: "n2");
        minValue.text = DataManager.visibleDataset.minValue.ToString(format: "n2");
        meanValue.text = DataManager.visibleDataset.mean.ToString(format: "n2");
    }
}
