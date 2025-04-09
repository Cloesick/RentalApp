import os

# Define the folder structure and corresponding files with code
structure = {
    "Authentication": {},
    "Listings": {},
    "Search": {},
    "Booking": {},
    "Payments": {},
    "Messaging": {},
    "Reviews": {},
    "Admin": {},
    "Utils": {},
    "Data": {
        "market_trends.py": """import requests

def fetch_market_data(api_url):
    \"\"\"Fetch real estate market data from an external API.\"\"\"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch market data")

def analyze_trends(data):
    \"\"\"Analyze trends in property prices and sales volume.\"\"\"
    trends = {
        "average_price": sum(item["price"] for item in data) / len(data),
        "total_sales": sum(item["sales"] for item in data),
    }
    return trends
""",
        "statistics.py": """import matplotlib.pyplot as plt

def visualize_data(data):
    \"\"\"Visualize data using charts.\"\"\"
    months = [item["month"] for item in data]
    occupancy_rates = [item["occupancy_rate"] for item in data]

    plt.bar(months, occupancy_rates)
    plt.title("Occupancy Rates by Month")
    plt.xlabel("Month")
    plt.ylabel("Occupancy Rate (%)")
    plt.show()
"""
    },
    "CustomerDemographics": {
        "customer_profiles.py": """def segment_customers(customers):
    \"\"\"Segment customers based on demographics.\"\"\"
    segments = {
        "foreign_investors": [c for c in customers if c["nationality"] != "Spain"],
        "holiday_renters": [c for c in customers if c["purpose"] == "holiday"],
    }
    return segments
"""
    },
    "SeasonalAnalysis": {
        "seasonal_demand.py": """def analyze_seasonal_demand(data):
    \"\"\"Analyze seasonal variations in demand.\"\"\"
    peak_season = max(data, key=lambda x: x["occupancy_rate"])
    off_peak_season = min(data, key=lambda x: x["occupancy_rate"])
    return {"peak_season": peak_season, "off_peak_season": off_peak_season}

def mitigate_risks():
    \"\"\"Mitigate risks of seasonal fluctuations.\"\"\"
    strategies = [
        "Diversify service offerings",
        "Implement flexible pricing",
        "Run targeted marketing campaigns",
    ]
    return strategies
"""
    },
    "CompetitiveAnalysis": {
        "competitor_analysis.py": """def fetch_competitors():
    \"\"\"Fetch competitor data from online directories.\"\"\"
    competitors = [
        {"name": "Company A", "services": ["Luxury Rentals"], "market_share": 25},
        {"name": "Company B", "services": ["Budget Rentals"], "market_share": 15},
    ]
    return competitors

def benchmark_competitors(competitors):
    \"\"\"Benchmark competitors' strengths and weaknesses.\"\"\"
    for competitor in competitors:
        print(f"Competitor: {competitor['name']}")
        print(f"Services: {', '.join(competitor['services'])}")
        print(f"Market Share: {competitor['market_share']}%")
        print("-" * 20)
""",
        "established_businesses.py": """def research_businesses():
    \"\"\"Research established property management businesses.\"\"\"
    businesses = [
        {"name": "Company A", "reputation": "Excellent", "services": ["Luxury Rentals"]},
        {"name": "Company B", "reputation": "Good", "services": ["Budget Rentals"]},
    ]
    return businesses

def analyze_best_practices(businesses):
    \"\"\"Analyze best practices of established businesses.\"\"\"
    for business in businesses:
        print(f"Business: {business['name']}")
        print(f"Reputation: {business['reputation']}")
        print(f"Services: {', '.join(business['services'])}")
        print("-" * 20)
"""
    },
    "Docs": {
        "marketstudy.doc": """Market Study: Property Management Business in Costa del Sol

Objective: To analyze the Costa del Sol's property management market, identifying key trends, competitive landscape, customer demographics, and seasonal impacts to inform business strategy.

I. Market Trends:
... (rest of the content from the document)
"""
    }
}

# Base directory for the project
base_dir = "c:\\Users\\nicol\\Projects\\RealEstateMalaga\\RentalApp"

# Function to create folders and files
def create_structure(base_path, structure):
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file_name, file_content in files.items():
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(file_content)

# Create the folder structure and files
create_structure(base_dir, structure)

print("Folder structure and files have been created successfully.")
