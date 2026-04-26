from typing import List
import re

STOP_WORDS = {
    "i", "me", "my", "we", "our", "you", "your",
    "he", "she", "it", "they", "them",
    "the", "a", "an", "and", "or", "but",
    "to", "of", "in", "on", "for", "with", "from", "at", "by",
    "this", "that", "these", "those",
    "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did",
    "very", "really", "quite", "just",
}

IMPORTANT_PHRASES = {
    "product quality",
    "customer service",
    "customer support",
    "friendly staff",
    "helpful staff",
    "bad experience",
    "great experience",
    "slow delivery",
    "fast delivery",
    "late delivery",
    "app crashed",
    "website crashed",
    "checkout problem",
    "payment issue",
    "refund issue",
    "delivery issue",
    "poor service",
}

BUSINESS_TERMS = {
    "product",
    "quality",
    "service",
    "staff",
    "support",
    "delivery",
    "shipping",
    "checkout",
    "website",
    "app",
    "price",
    "payment",
    "experience",
    "customer",
    "order",
    "refund",
    "return",
}


def extract_keywords(text: str) -> List[str]:
    normalized_text = text.lower()

    # Remove punctuation and symbols, and normalize spaces
    cleaned_text = re.sub(r"[^a-zA-Z\s]", " ", normalized_text)
    cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()

    keywords = []

    # Extract important phrases
    for phrase in IMPORTANT_PHRASES:
        if phrase in cleaned_text:
            keywords.append(phrase)

    # Find all individual words
    words = re.findall(r"\b[a-zA-Z]+\b", cleaned_text)

    for word in words:
        if word in STOP_WORDS:
            continue

        # Extract business terms
        if word in BUSINESS_TERMS:
            keywords.append(word)
            continue

        # Keep descriptive words
        if len(word) > 3:
            keywords.append(word)

    # Remove duplicates
    return list(dict.fromkeys(keywords))