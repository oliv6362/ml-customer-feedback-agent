# Customer Feedback Analysis Agent

A simple AutoGen project that analyzes customer feedback and generates actionable business insights.

The agent processes feedback by:

- Reading customer feedback from a local feedback store
- Analyzing sentiment
- Extracting keywords
- Categorizing feedback into predefined themes
- Generating actionable insights and a manager notification draft

## Tools

The project is split into small tools:

- **Feedback Reader Tool:** returns sample customer feedback
- **Sentiment Analysis Tool:** classifies feedback as positive, negative, or neutral
- **Keyword Extraction Tool:** extracts business-relevant words and phrases
- **Categorization Tool:** maps keywords to predefined categories
- **Feedback Processing Tool:** runs the full processing pipeline
- **Insight Generation Tool:** uses an LLM to summarize insights and recommend actions

## Architecture

The main AutoGen agent uses two high-level tools:

- **feedback_processing:** reads, analyzes, extracts keywords, and categorizes all feedback
- **insight_generation:** generates business insights from the processed feedback

The smaller tools are used internally by the feedback processing tool, which keeps the agent workflow simple and reliable.

## Prerequisites

- Make sure Ollama is running locally and that you have pulled an Ollama model, for example gemma4:latest.  
- Have Python 3.10-3.12 installed

## Installation

Install Python dependencies:

    pip install -r requirements.txt

## Configuration

Create a local configuration file:

    feedback_agent/config.py

Example local Ollama configuration:

    LLM_CONFIG = {
        "config_list": [
            {
                "model": "gemma4:latest",
                "api_type": "ollama",
                "client_host": "http://127.0.0.1:11434",
                "options": {
                    "temperature": 0.1,
                    "seed": 42,
                }
            }
        ],
        "cache_seed": None,
    }

For local Ollama usage, make sure Ollama is running at:

    http://127.0.0.1:11434

## Run the agent

From the project root, run:

    python -m feedback_agent.agent.feedback_analysis_agent
