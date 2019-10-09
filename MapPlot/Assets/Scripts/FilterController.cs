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
        GameObject.Find("ApplyFilter_Button").GetComponentInChildren<Text>().text = "Apply filters";
        GameObject.Find("ResetFilter_Button").GetComponentInChildren<Text>().text = "Reset filters";

        if(DataManager.visibleDataset == null)
        {
            return;
        }
        maxTemp.maxValue = Mathf.CeilToInt(DataManager.visibleDataset.maxValue);
        maxTemp.minValue = Mathf.FloorToInt(DataManager.visibleDataset.minValue);
        maxTemp.value = DataManager.visibleDataset.maxValue;

        minTemp.maxValue = Mathf.CeilToInt(DataManager.visibleDataset.maxValue);
        minTemp.minValue = Mathf.FloorToInt(DataManager.visibleDataset.minValue);
        minTemp.value = DataManager.visibleDataset.minValue;

        maxIndicator.text = DataManager.visibleDataset.maxValue.ToString(format: "n2");
        minIndicator.text = DataManager.visibleDataset.minValue.ToString(format: "n2");
    }

    private void Interlock()
    {
        if(maxTemp.value < minTemp.value)
        {
            maxTemp.value = minTemp.value;
        }
        else if(minTemp.value > maxTemp.value)
        {
            minTemp.value = maxTemp.value;
        }
    }

    public void UpdateFilterValues()
    {
        Interlock();
        DataManager.SetMinFilter(minTemp.value);
        DataManager.SetMaxFilter(maxTemp.value);
        maxIndicator.text = maxTemp.value.ToString("n2");
        minIndicator.text = minTemp.value.ToString("n2");
    }

    public void ApplyFilter()
    {
        DataManager.FilterDataset();
    }

    public void ResetFilterController()
    {
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
