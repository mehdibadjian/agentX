# ai_consultancy_agents.py

from openai import OpenAI
from typing import List, Dict, Optional
import logging
import json
import os
from datetime import datetime
from dataclasses import dataclass
from enum import Enum
import yaml
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ai_consultancy.log'),
        logging.StreamHandler()
    ]
)

class ModelType(Enum):
    GPT4 = "gpt-4"
    GPT35 = "gpt-3.5-turbo"
    GPT4_TURBO = "gpt-4-turbo-preview"

@dataclass
class AgentConfig:
    name: str
    role_description: str
    responsibilities: List[str]
    model: ModelType
    temperature: float = 0.7
    max_tokens: int = 1000

class ConversationHistory:
    def __init__(self):
        self.messages: List[Dict[str, str]] = []
        self.timestamp = datetime.now()

    def add_message(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})

    def get_messages_for_api(self):
        return [{"role": m["role"], "content": m["content"]} for m in self.messages]

    def save_to_file(self, filename: str):
        Path("conversations").mkdir(exist_ok=True)
        filepath = Path("conversations") / filename
        with open(filepath, 'w') as f:
            json.dump({
                "messages": self.messages,
                "timestamp": str(self.timestamp)
            }, f, indent=2)

class AIAgent:
    def __init__(self, config: AgentConfig):
        self.config = config
        self.conversation = ConversationHistory()
        self.logger = logging.getLogger(f"Agent_{self.config.name}")
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OpenAI API key not found in environment variables")
        self.client = OpenAI(api_key=api_key)

    def generate_system_message(self) -> str:
        return (
            f"You are {self.config.name}, {self.config.role_description}.\n"
            "Your responsibilities include:\n"
            + "\n".join(f"{idx}. {resp}" for idx, resp in enumerate(self.config.responsibilities, 1))
        )

    def get_response(self, user_input: Optional[str] = None) -> str:
        try:
            # Initialize conversation with system message if empty
            if not self.conversation.messages:
                self.conversation.add_message("system", self.generate_system_message())

            # Add user input if provided
            if user_input:
                self.conversation.add_message("user", user_input)

            # Get messages in correct format for API
            messages = self.conversation.get_messages_for_api()

            # Make API call
            response = self.client.chat.completions.create(
                model=self.config.model.value,
                messages=messages,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens
            )

            assistant_message = response.choices[0].message.content.strip()
            self.conversation.add_message("assistant", assistant_message)
            return assistant_message

        except Exception as e:
            error_msg = f"Error generating response: {str(e)}"
            self.logger.error(error_msg)
            raise RuntimeError(error_msg)

class AIConsultancy:
    def __init__(self, config_path: str):
        self.logger = logging.getLogger("AIConsultancy")
        self.load_config(config_path)
        self.agents: Dict[str, AIAgent] = {}
        self.initialize_agents()

    def load_config(self, config_path: str):
        try:
            with open(config_path, 'r') as f:
                self.config = yaml.safe_load(f)
        except FileNotFoundError:
            self.logger.error(f"Configuration file not found: {config_path}")
            raise
        except yaml.YAMLError as e:
            self.logger.error(f"Error parsing configuration file: {e}")
            raise

    def initialize_agents(self):
        for agent_config in self.config['agents']:
            try:
                config = AgentConfig(
                    name=agent_config['name'],
                    role_description=agent_config['role_description'],
                    responsibilities=agent_config['responsibilities'],
                    model=ModelType[agent_config['model']],
                    temperature=agent_config.get('temperature', 0.7),
                    max_tokens=agent_config.get('max_tokens', 1000)
                )
                self.agents[config.name] = AIAgent(config)
                self.logger.info(f"Initialized agent: {config.name}")
            except Exception as e:
                self.logger.error(f"Error initializing agent {agent_config.get('name', 'unknown')}: {str(e)}")
                raise

    def process_client_request(self, client_input: str) -> Dict[str, str]:
        responses = {}
        for agent_name, agent in self.agents.items():
            try:
                self.logger.info(f"Processing with {agent_name}")
                response = agent.get_response(client_input)
                responses[agent_name] = response

                filename = f"conversation_{agent_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                agent.conversation.save_to_file(filename)
                self.logger.info(f"Saved conversation history for {agent_name}")
            except Exception as e:
                error_msg = f"Error processing request with {agent_name}: {str(e)}"
                self.logger.error(error_msg)
                responses[agent_name] = f"Error: {error_msg}"

        return responses

def main():
    try:
        # Ensure config.yaml exists in the current directory
        if not Path("config.yaml").exists():
            raise FileNotFoundError("config.yaml not found in current directory")

        # Initialize the consultancy
        consultancy = AIConsultancy("config.yaml")

        # Example client input
        client_input = "I want to build a scalable crypto currency app that can have the highest chance of winning"

        # Process the request
        responses = consultancy.process_client_request(client_input)

        # Print responses
        for agent_name, response in responses.items():
            print(f"\n--- Response from {agent_name} ---")
            print(response)

    except Exception as e:
        logging.error(f"Main execution error: {str(e)}")
        raise

if __name__ == "__main__":
    main()