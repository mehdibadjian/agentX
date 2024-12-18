# agents/business_analyst_agent.py

from agentx.ai_agent import AIAgent
from agentx.ai_model_provider import AIModelProvider


class BusinessAnalystAgent(AIAgent):
    def __init__(self, ai_provider: AIModelProvider):
        super().__init__(
            name="AI Business Analyst",
            role_description="who gathers and analyzes client requirements.",
            responsibilities=[
                "Document business processes",
                "Ensure solutions meet business needs",
            ],
            model="gpt-3.5-turbo",
            ai_provider=ai_provider,
        )