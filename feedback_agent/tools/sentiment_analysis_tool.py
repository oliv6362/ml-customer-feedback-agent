from typing import Literal

Sentiment = Literal["positive", "negative", "neutral"]

POSITIVE_WORDS = {
    "love",
    "great",
    "good",
    "excellent",
    "amazing",
    "happy",
    "satisfied",
    "friendly",
    "helpful",
}

NEGATIVE_WORDS = {
    "bad",
    "terrible",
    "poor",
    "awful",
    "hate",
    "broken",
    "slow",
    "crash",
    "issue",
    "problem",
    "angry",
    "disappointed",
}

def analyze_sentiment(text: str) -> Sentiment:
    normalized_text = text.lower()

    positive_score = sum(word in normalized_text for word in POSITIVE_WORDS)
    negative_score = sum(word in normalized_text for word in NEGATIVE_WORDS)

    if positive_score > negative_score:
        return "positive"

    if negative_score > positive_score:
        return "negative"

    return "neutral"