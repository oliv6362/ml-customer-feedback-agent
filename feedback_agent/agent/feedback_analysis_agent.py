from autogen import ConversableAgent
from feedback_agent.tools.insight_generation_tool import generate_insights
from feedback_agent.tools.feedback_processing_tool import process_feedback
from feedback_agent.config import LLM_CONFIG

def create_feedback_analysis_agent() -> ConversableAgent:
    # define the agent
    feedback_analysis_agent = ConversableAgent(
        name="Feedback Analysis Agent",
        system_message="You are a helpful AI assistant that analyzes customer feedback. "
                       "You can process all customer feedback using the feedback_processing tool. "
                       "The feedback_processing tool reads feedback, analyzes sentiment, extracts keywords, "
                       "and categorizes feedback using predefined categories. "
                       "You can generate actionable insights using the insight_generation tool. "
                       "When the task is complete, return the processed feedback and insights "
                       "Don't include any other text in your response. "
                       "Return 'TERMINATE' when the task is done.",
        llm_config=LLM_CONFIG,
    )

    # add the tools to the agent
    feedback_analysis_agent.register_for_llm(name="feedback_processing", description="Read, analyze sentiment, extract keywords, and categorize all customer feedback")(process_feedback)
    feedback_analysis_agent.register_for_llm(name="insight_generation", description="Generate actionable business insights from processed customer feedback")(generate_insights)

    return feedback_analysis_agent

def create_user_proxy():
    user_proxy = ConversableAgent(
        name="User",
        llm_config=False,
        is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
        human_input_mode="NEVER",
    )
    user_proxy.register_for_execution(name="feedback_processing")(process_feedback)
    user_proxy.register_for_execution(name="insight_generation")(generate_insights)

    return user_proxy



def main():
    user_proxy = create_user_proxy()
    feedback_analysis_agent = create_feedback_analysis_agent()

    user_proxy.initiate_chat(
        feedback_analysis_agent,
        message="""
                1. Process all feedback using the feedback_processing tool.
                2. Generate actionable insights from the processed feedback using the insight_generation tool.
                3. Return both:
                   - the processed feedback JSON array
                   - the generated insights

                Return only the processed feedback and insights.
                """
    )

if __name__ == "__main__":
    main()
