# agents/it_consultant_agent.py

from agentx.ai_agent import AIAgent
from agentx.ai_model_provider import AIModelProvider


class ITConsultantAgent(AIAgent):
    def __init__(self, ai_provider: AIModelProvider):
        super().__init__(
            name="AI IT Consultant",
            role_description="who assesses client IT environments and provides strategic advice.",
            responsibilities=[
                "Identify issues and areas for improvement",
                "Recommend technology solutions aligning with business goals",
            ],
            model="gpt-4",
            ai_provider=ai_provider,
        )