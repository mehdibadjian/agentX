# agents/project_manager_agent.py

from ai_agent import AIAgent
from ai_model_provider import AIModelProvider


class ProjectManagerAgent(AIAgent):
    def __init__(self, ai_provider: AIModelProvider):
        super().__init__(
            name="AI Project Manager",
            role_description="who oversees project planning and execution.",
            responsibilities=[
                "Coordinate between different AI agents",
                "Monitor timelines and deliverables",
                "Communicate progress to stakeholders",
            ],
            model="gpt-4",
            ai_provider=ai_provider,
        )