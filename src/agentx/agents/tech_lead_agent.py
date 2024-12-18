# agents/tech_lead_agent.py

from agentx.ai_agent import AIAgent
from agentx.ai_model_provider import AIModelProvider


class TechLeadAgent(AIAgent):
    def __init__(self, ai_provider: AIModelProvider):
        super().__init__(
            name="AI Tech Lead",
            role_description="who oversees technical development.",
            responsibilities=[
                "Lead development teams",
                "Ensure code quality and best practices",
                "Coordinate technical solutions",
            ],
            model="gpt-4",
            ai_provider=ai_provider,
        )