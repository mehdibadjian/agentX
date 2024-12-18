# agents/devops_lead_agent.py

from agentx.ai_agent import AIAgent
from agentx.ai_model_provider import AIModelProvider


class DevOpsLeadAgent(AIAgent):
    def __init__(self, ai_provider: AIModelProvider):
        super().__init__(
            name="AI DevOps Lead",
            role_description="who oversees the DevOps processes.",
            responsibilities=[
                "Implement CI/CD pipelines",
                "Ensure system reliability and scalability",
                "Automate infrastructure management",
            ],
            model="gpt-4",
            ai_provider=ai_provider,
        )