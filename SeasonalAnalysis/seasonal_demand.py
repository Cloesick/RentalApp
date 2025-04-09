def analyze_seasonal_demand(data):
    """Analyze seasonal variations in demand."""
    peak_season = max(data, key=lambda x: x["occupancy_rate"])
    off_peak_season = min(data, key=lambda x: x["occupancy_rate"])
    return {"peak_season": peak_season, "off_peak_season": off_peak_season}

def mitigate_risks():
    """Mitigate risks of seasonal fluctuations."""
    strategies = [
        "Diversify service offerings",
        "Implement flexible pricing",
        "Run targeted marketing campaigns",
    ]
    return strategies
