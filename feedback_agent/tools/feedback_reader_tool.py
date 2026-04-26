from typing import List, TypedDict, Literal

class Feedback(TypedDict):
    id: str
    text: str
    source: Literal["email", "chat", "survey"]

feedback_store: List[Feedback] = [
    {
        "id": "1",
        "text": "I love the product. The quality feels excellent.",
        "source": "email",
    },
    {
        "id": "2",
        "text": "The delivery was slow and my order arrived late.",
        "source": "chat",
    },
    {
        "id": "3",
        "text": "The staff was friendly and very helpful.",
        "source": "survey",
    },
    {
        "id": "4",
        "text": "The app crashed during checkout and payment failed.",
        "source": "survey",
    },
    {
        "id": "5",
        "text": "Customer support never replied to my refund issue.",
        "source": "email",
    },
]

def query_feedback() -> List[Feedback]:
    return feedback_store