import matplotlib.pyplot as plt

def visualize_data(data):
    """Visualize data using charts."""
    months = [item["month"] for item in data]
    occupancy_rates = [item["occupancy_rate"] for item in data]

    plt.bar(months, occupancy_rates)
    plt.title("Occupancy Rates by Month")
    plt.xlabel("Month")
    plt.ylabel("Occupancy Rate (%)")
    plt.show()
