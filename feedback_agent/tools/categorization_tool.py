from typing import List

CATEGORY_KEYWORDS = {
    "Product Quality": {
        "quality",
        "product quality",
        "broken",
        "defect",
        "durable",
        "damaged",
        "poor quality",
    },
    "Quality of Service": {
        "service",
        "customer service",
        "customer support",
        "support",
        "poor service",
        "helpful",
        "helpful staff",
    },
    "Staff": {
        "staff",
        "friendly",
        "friendly staff",
        "employee",
        "employees",
    },
    "Delivery": {
        "delivery",
        "shipping",
        "slow delivery",
        "fast delivery",
        "late delivery",
        "late",
        "slow",
    },
    "App/Website": {
        "app",
        "website",
        "checkout",
        "app crashed",
        "website crashed",
        "checkout problem",
        "payment",
        "payment issue",
        "crashed",
    },
    "Price": {
        "price",
        "expensive",
        "cheap",
        "cost",
        "pricing",
    },
    "Returns/Refunds": {
        "refund",
        "return",
        "refund issue",
        "return issue",
    },
    "Customer Experience": {
        "experience",
        "great experience",
        "bad experience",
        "satisfied",
        "disappointed",
        "happy",
        "love",
        "great",
        "bad",
    },
}


def categorize_feedback(keywords: List[str]) -> List[str]:
    normalized_keywords = {keyword.lower().strip() for keyword in keywords}

    categories = []

    # Loop through each category and check if any extracted keyword matches it
    for category, category_keywords in CATEGORY_KEYWORDS.items():
        if normalized_keywords.intersection(category_keywords):
            categories.append(category)

    # Fallback
    if not categories:
        categories.append("Other")

    return categories