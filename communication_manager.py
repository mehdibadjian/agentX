# communication_manager.py

from typing import List, Dict
from ai_agent import AIAgent
import logging


class CommunicationManager:
    def __init__(self, agents: List[AIAgent]):
        self.agents = agents
        self.messages: List[Dict[str, str]] = []

    def broadcast_message(self, sender: AIAgent, content: str):
        """Broadcasts a message to all agents except the sender."""
        message = {'role': 'assistant', 'content': content}
        self.messages.append(message)
        logging.info(f"Broadcasting message from {sender.name}")

        for agent in self.agents:
            if agent != sender:
                agent.receive_message(message)

    def review_and_collate_responses(self) -> str:
        """Aggregates responses from agents and compiles the final output."""
        combined_content = ""
        for agent in self.agents:
            if hasattr(agent, 'latest_response'):
                combined_content += f"### {agent.name}\n{agent.latest_response}\n\n"
        return combined_content