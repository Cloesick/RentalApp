def fetch_competitors():
    """Fetch competitor data from online directories."""
    competitors = [
        {"name": "Company A", "services": ["Luxury Rentals"], "market_share": 25},
        {"name": "Company B", "services": ["Budget Rentals"], "market_share": 15},
    ]
    return competitors

def benchmark_competitors(competitors):
    """Benchmark competitors' strengths and weaknesses."""
    for competitor in competitors:
        print(f"Competitor: {competitor['name']}")
        print(f"Services: {', '.join(competitor['services'])}")
        print(f"Market Share: {competitor['market_share']}%")
        print("-" * 20)
