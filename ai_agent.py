# ai_agent.py

from typing import List, Dict
from ai_model_provider import AIModelProvider
import logging


class AIAgent:
    def __init__(
        self,
        name: str,
        role_description: str,
        responsibilities: List[str],
        model: str,
        ai_provider: AIModelProvider,
        temperature: float = 0.7,
    ):
        self.name = name
        self.role_description = role_description
        self.responsibilities = responsibilities
        self.model = model
        self.temperature = temperature
        self.messages: List[Dict[str, str]] = []
        self.ai_provider = ai_provider
        self.latest_response: str = ""

    def generate_system_message(self) -> Dict[str, str]:
        # Construct the system prompt
        system_content = f"You are {self.name}, {self.role_description}\n"
        system_content += "Your responsibilities include:\n"
        for idx, responsibility in enumerate(self.responsibilities, start=1):
            system_content += f"{idx}. {responsibility}\n"
        return {"role": "system", "content": system_content}

    def get_response(self, user_input: str = "") -> str:
        # Prepare messages
        if not self.messages:
            system_message = self.generate_system_message()
            self.messages.append(system_message)
            logging.debug(f"{self.name} system message: {system_message['content']}")

        if user_input:
            user_message = {"role": "user", "content": user_input}
            self.messages.append(user_message)
            logging.debug(f"User input to {self.name}: {user_input}")

        assistant_message = self.ai_provider.generate_response(
            messages=self.messages,
            model=self.model,
            temperature=self.temperature,
        )

        # Append assistant's response
        self.messages.append({"role": "assistant", "content": assistant_message})
        self.latest_response = assistant_message
        logging.debug(f"{self.name} response: {assistant_message}")

        return assistant_message

    def receive_message(self, message: Dict[str, str]):
        # Agents can receive messages from others
        self.messages.append(message)
        logging.debug(f"{self.name} received message: {message['content']}")