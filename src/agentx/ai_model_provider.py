# ai_model_provider.py

from abc import ABC, abstractmethod
from typing import List, Dict


class AIModelProvider(ABC):
    @abstractmethod
    def generate_response(
        self, messages: List[Dict[str, str]], model: str, temperature: float
    ) -> str:
        """Generate a response from the AI model.

        Args:
            messages (List[Dict[str, str]]): A list of messages in the conversation.
            model (str): The model name.
            temperature (float): Sampling temperature.

        Returns:
            str: The assistant's response.
        """
        pass