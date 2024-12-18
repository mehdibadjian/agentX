# agents/solution_architect_agent.py

from agentx.ai_agent import AIAgent
from agentx.ai_model_provider import AIModelProvider


class SolutionArchitectAgent(AIAgent):
    def __init__(self, ai_provider: AIModelProvider):
        super().__init__(
            name="AI Solution Architect",
            role_description="who designs IT system architectures.",
            responsibilities=[
                "Select appropriate technologies and platforms",
                "Ensure scalability and security of solutions",
                "Provide technical oversight during implementation",
            ],
            model="gpt-4",
            ai_provider=ai_provider,
        )