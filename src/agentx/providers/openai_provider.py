import openai
import os
from typing import List, Dict
from agentx.ai_model_provider import AIModelProvider
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()


class OpenAIProvider(AIModelProvider):
    def __init__(self):
        # Set up OpenAI API key securely
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OpenAI API key not found in environment variables.")
        openai.api_key = api_key

    def generate_response(
        self, messages: List[Dict[str, str]], model: str, temperature: float
    ) -> str:
        try:
            # Use client instance and chat completions endpoint
            client = openai.OpenAI()
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
            )
            assistant_message = response.choices[0].message.content.strip()
            return assistant_message
        except openai.OpenAIError as e:
            logging.error(f"OpenAI API error: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            raise