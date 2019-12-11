using UnityEngine;
using UnityEngine.UI;

public class FilterController : MonoBehaviour
{
    public Slider maxTemp;
    public Slider minTemp;

    public Text maxIndicator;
    public Text minIndicator;

    // Start is called before the first frame update
    void Start()
    {   
        // Sets buttons text properties
        GameObject.Find("ApplyFilter_Button").GetComponentInChildren<Text>().text = "Apply filters";
        GameObject.Find("ResetFilter_Button").GetComponentInChildren<Text>().text = "Reset filters";

        if(DataManager.visibleDataset == null)
        {
            return;
        }
        // Defines minimum and maximum values on the filter sliders.
        maxTemp.maxValue = Mathf.CeilToInt(DataManager.visibleDataset.maxValue);
        maxTemp.minValue = Mathf.FloorToInt(DataManager.visibleDataset.minValue);
        maxTemp.value = DataManager.visibleDataset.maxValue;

        minTemp.maxValue = Mathf.CeilToInt(DataManager.visibleDataset.maxValue);
        minTemp.minValue = Mathf.FloorToInt(DataManager.visibleDataset.minValue);
        minTemp.value = DataManager.visibleDataset.minValue;
        // Defines the value labels
        maxIndicator.text = DataManager.visibleDataset.maxValue.ToString(format: "n2");
        minIndicator.text = DataManager.visibleDataset.minValue.ToString(format: "n2");
    }

    public void UpdateFilterValues()
    {   
        // Changes values of the filters
        DataManager.SetMinFilter(minTemp.value);
        DataManager.SetMaxFilter(maxTemp.value);
        maxIndicator.text = maxTemp.value.ToString("n2");
        minIndicator.text = minTemp.value.ToString("n2");
    }

    public void ApplyFilter()
    {
        // Apllies the filters to the dataset
        DataManager.FilterDataset();
    }

    public void ResetFilterController()
    {
        // This function resets all filter values and restores the dataset to the original
        DataManager.ResetFilters();
        maxTemp.maxValue = Mathf.CeilToInt(DataManager.visibleDataset.maxValue);
        maxTemp.minValue = Mathf.FloorToInt(DataManager.visibleDataset.minValue);
        maxTemp.value = DataManager.visibleDataset.maxValue;

        minTemp.maxValue = Mathf.CeilToInt(DataManager.visibleDataset.maxValue);
        minTemp.minValue = Mathf.FloorToInt(DataManager.visibleDataset.minValue);
        minTemp.value = DataManager.visibleDataset.minValue;

        maxIndicator.text = DataManager.visibleDataset.maxValue.ToString(format: "n2");
        minIndicator.text = DataManager.visibleDataset.minValue.ToString(format: "n2");
    }
}
