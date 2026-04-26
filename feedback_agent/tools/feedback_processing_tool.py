from typing import Any, Dict, List

from feedback_agent.tools.feedback_reader_tool import query_feedback
from feedback_agent.tools.sentiment_analysis_tool import analyze_sentiment
from feedback_agent.tools.keyword_extraction_tool import extract_keywords
from feedback_agent.tools.categorization_tool import categorize_feedback


def process_feedback() -> List[Dict[str, Any]]:
    feedback_items = query_feedback()
    processed_feedback = []

    for item in feedback_items:
        text = item["text"]
        keywords = extract_keywords(text)
        sentiment = analyze_sentiment(text)
        categories = categorize_feedback(keywords)

        processed_feedback.append({
            "id": item["id"],
            "source": item["source"],
            "text": text,
            "sentiment": sentiment,
            "keywords": keywords,
            "categories": categories,
        })

    return processed_feedback