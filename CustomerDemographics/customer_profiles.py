def segment_customers(customers):
    """Segment customers based on demographics."""
    segments = {
        "foreign_investors": [c for c in customers if c["nationality"] != "Spain"],
        "holiday_renters": [c for c in customers if c["purpose"] == "holiday"],
    }
    return segments
