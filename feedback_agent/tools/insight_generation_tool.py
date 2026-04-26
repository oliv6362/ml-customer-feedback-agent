from typing import List, Dict, Any
from autogen import AssistantAgent
from feedback_agent.config import LLM_CONFIG


def generate_insights(processed_feedback: List[Dict[str, Any]]) -> str:
    insight_generation_agent = AssistantAgent(
        name="Insight Generation Agent",
        system_message=(
            "You are a business analyst assistant. "
            "You summarize processed customer feedback into actionable business insights. "
            "Focus on recurring themes, sentiment patterns, risks, and concrete improvement actions. "
            "Do not overstate conclusions. If the dataset is small or feedback is vague, clearly state that the insight is tentative. "
            "Write clearly and concisely. "
            "Do not include TERMINATE."
        ),
        llm_config=LLM_CONFIG,
    )

    reply = insight_generation_agent.generate_reply(
        messages=[
            {
                "role": "user",
                "content": (
                    "Generate actionable business insights from this processed customer feedback:\n"
                    f"{processed_feedback}\n\n"
                    "Return the result with these sections:\n"
                    "1. Summary\n"
                    "2. Main themes\n"
                    "3. Recommended actions\n"
                    "4. Manager notification draft"
                ),
            }
        ],
    )

    if not reply:
        raise ValueError("No reply found")

    if isinstance(reply, dict):
        reply_content = reply.get("content")
        if not reply_content:
            raise ValueError("No content found in the reply")
        return reply_content.strip()

    return str(reply).strip()