import requests

def fetch_market_data(api_url):
    """Fetch real estate market data from an external API."""
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch market data")

def analyze_trends(data):
    """Analyze trends in property prices and sales volume."""
    trends = {
        "average_price": sum(item["price"] for item in data) / len(data),
        "total_sales": sum(item["sales"] for item in data),
    }
    return trends
