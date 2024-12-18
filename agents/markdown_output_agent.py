# agents/markdown_output_agent.py

from ai_agent import AIAgent
from ai_model_provider import AIModelProvider


class MarkdownOutputAgent(AIAgent):
    def __init__(self, ai_provider: AIModelProvider):
        super().__init__(
            name="AI Markdown Output Agent",
            role_description="who formats the final response into a Markdown document.",
            responsibilities=[
                "Compile responses from all agents",
                "Format content using Markdown syntax",
                "Ensure clarity and professionalism in the document",
            ],
            model="gpt-4",
            ai_provider=ai_provider,
        )

    def format_to_markdown(self, content: str) -> str:
        # The agent ensures the content is properly formatted in Markdown
        formatted_content = f"# Final Report\n\n{content}"
        return formatted_content

    def get_response(self, aggregated_content: str) -> str:
        # Override to directly format the aggregated content
        self.latest_response = self.format_to_markdown(aggregated_content)
        return self.latest_response