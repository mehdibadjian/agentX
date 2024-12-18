# communication_manager.py

from typing import List, Dict, Set
from ai_agent import AIAgent
import logging
from enum import Enum
import re


class TopicCategory(Enum):
    BUSINESS = "business"
    TECHNICAL = "technical"
    SECURITY = "security"
    INFRASTRUCTURE = "infrastructure"
    DEVELOPMENT = "development"
    PROJECT_MANAGEMENT = "project_management"
    ARCHITECTURE = "architecture"
    DEVOPS = "devops"


class CommunicationManager:
    def __init__(self, agents: List[AIAgent], ai_provider):
        self.agents = agents
        self.messages: List[Dict[str, str]] = []
        self.ai_provider = ai_provider
        self.agent_topics = self._initialize_agent_topics()

    def _initialize_agent_topics(self) -> Dict[str, Set[TopicCategory]]:
        """Initialize which topics each agent is interested in."""
        return {
            "AI Business Analyst": {
                TopicCategory.BUSINESS, 
                TopicCategory.PROJECT_MANAGEMENT
            },
            "AI IT Consultant": {
                TopicCategory.TECHNICAL, 
                TopicCategory.SECURITY, 
                TopicCategory.BUSINESS
            },
            "AI Solution Architect": {
                TopicCategory.ARCHITECTURE, 
                TopicCategory.TECHNICAL, 
                TopicCategory.SECURITY
            },
            "AI Project Manager": {
                TopicCategory.PROJECT_MANAGEMENT, 
                TopicCategory.BUSINESS
            },
            "AI DevOps Lead": {
                TopicCategory.DEVOPS, 
                TopicCategory.INFRASTRUCTURE, 
                TopicCategory.SECURITY
            },
            "AI Tech Lead": {
                TopicCategory.DEVELOPMENT, 
                TopicCategory.TECHNICAL, 
                TopicCategory.ARCHITECTURE
            },
            "AI Markdown Output Agent": set()  # Receives final compiled output only
        }

    def _analyze_message_content(self, content: str) -> Set[TopicCategory]:
        """
        Analyze message content to determine relevant topics.
        Uses keyword matching and potentially AI analysis for complex content.
        """
        topics = set()

        # Keywords for each category
        keywords = {
            TopicCategory.BUSINESS: [
                "business", "cost", "roi", "stakeholder", "requirement", 
                "process", "workflow", "budget"
            ],
            TopicCategory.TECHNICAL: [
                "technical", "technology", "system", "software", "database", 
                "api", "integration"
            ],
            TopicCategory.SECURITY: [
                "security", "authentication", "authorization", "encryption", 
                "vulnerability", "threat"
            ],
            TopicCategory.INFRASTRUCTURE: [
                "infrastructure", "cloud", "server", "network", "hosting", 
                "scaling", "deployment"
            ],
            TopicCategory.DEVELOPMENT: [
                "development", "coding", "programming", "testing", "git", 
                "version control", "code review"
            ],
            TopicCategory.PROJECT_MANAGEMENT: [
                "timeline", "milestone", "resource", "planning", "coordination", 
                "schedule", "risk"
            ],
            TopicCategory.ARCHITECTURE: [
                "architecture", "design pattern", "system design", "scalability", 
                "microservice", "component"
            ],
            TopicCategory.DEVOPS: [
                "devops", "ci/cd", "pipeline", "automation", "monitoring", 
                "deployment", "container"
            ]
        }

        # Check for keywords in content
        content_lower = content.lower()
        for category, category_keywords in keywords.items():
            if any(keyword in content_lower for keyword in category_keywords):
                topics.add(category)

        # If no topics were identified through keywords, use AI analysis
        if not topics:
            topics = self._ai_analyze_content(content)

        return topics

    def _ai_analyze_content(self, content: str) -> Set[TopicCategory]:
        """
        Use AI to analyze content when keyword matching is insufficient.
        """
        prompt = f"""
        Analyze the following content and categorize it into one or more of these categories:
        - Business
        - Technical
        - Security
        - Infrastructure
        - Development
        - Project Management
        - Architecture
        - DevOps

        Content: {content}

        Return only the category names, separated by commas.
        """

        try:
            response = self.ai_provider.generate_response(
                messages=[{"role": "user", "content": prompt}],
                model="gpt-3.5-turbo",
                temperature=0.3
            )

            # Convert AI response to TopicCategory enum values
            categories = set()
            for category in response.split(','):
                category = category.strip().lower().replace(' ', '_')
                try:
                    categories.add(TopicCategory(category))
                except ValueError:
                    logging.warning(f"Invalid category received from AI: {category}")

            return categories
        except Exception as e:
            logging.error(f"Error in AI content analysis: {e}")
            # Return empty set if AI analysis fails
            return set()

    def _get_relevant_agents(self, topics: Set[TopicCategory], sender: AIAgent) -> List[AIAgent]:
        """
        Determine which agents should receive the message based on topics.
        """
        relevant_agents = []
        for agent in self.agents:
            # Skip the sender and Markdown Output Agent
            if agent == sender or agent.name == "AI Markdown Output Agent":
                continue

            # Check if agent's topics overlap with message topics
            agent_topics = self.agent_topics.get(agent.name, set())
            if agent_topics & topics:  # Set intersection
                relevant_agents.append(agent)

        return relevant_agents

    def broadcast_message(self, sender: AIAgent, content: str):
        """
        Intelligently broadcast message to relevant agents based on content analysis.
        """
        message = {'role': 'assistant', 'content': content, 'sender': sender.name}
        self.messages.append(message)

        # Analyze message content
        topics = self._analyze_message_content(content)
        logging.info(f"Message topics identified: {[topic.value for topic in topics]}")

        # Get relevant agents
        relevant_agents = self._get_relevant_agents(topics, sender)
        logging.info(f"Relevant agents for message: {[agent.name for agent in relevant_agents]}")

        # Broadcast to relevant agents
        for agent in relevant_agents:
            try:
                agent.receive_message(message)
                logging.info(f"Message from {sender.name} sent to {agent.name}")
            except Exception as e:
                logging.error(f"Error sending message to {agent.name}: {e}")

    def review_and_collate_responses(self) -> str:
        """
        Aggregate and organize responses from all agents into a coherent output.
        """
        sections = {
            "Business Analysis": [],
            "Technical Assessment": [],
            "Architecture & Design": [],
            "Implementation & DevOps": [],
            "Project Management": [],
        }

        # Categorize responses into sections
        for agent in self.agents:
            if not hasattr(agent, 'latest_response') or not agent.latest_response:
                continue

            response = agent.latest_response
            if "Business Analyst" in agent.name:
                sections["Business Analysis"].append(
                    f"### Business Analysis\n{response}"
                )
            elif "IT Consultant" in agent.name:
                sections["Technical Assessment"].append(
                    f"### Technical Assessment\n{response}"
                )
            elif "Solution Architect" in agent.name or "Tech Lead" in agent.name:
                sections["Architecture & Design"].append(
                    f"### {agent.name} Assessment\n{response}"
                )
            elif "DevOps Lead" in agent.name:
                sections["Implementation & DevOps"].append(
                    f"### DevOps Strategy\n{response}"
                )
            elif "Project Manager" in agent.name:
                sections["Project Management"].append(
                    f"### Project Planning\n{response}"
                )

        # Compile final report
        final_report = "# IT Consultancy Report\n\n"
        final_report += "## Executive Summary\n\n"

        # Add sections with content
        for section_title, content_list in sections.items():
            if content_list:
                final_report += f"## {section_title}\n\n"
                final_report += "\n\n".join(content_list) + "\n\n"

        final_report += "\n## Next Steps\n\n"
        final_report += "1. Review and approve proposed solutions\n"
        final_report += "2. Define implementation timeline\n"
        final_report += "3. Allocate resources\n"
        final_report += "4. Begin implementation phase\n\n"

        return final_report

    def get_message_history(self) -> List[Dict[str, str]]:
        """
        Return the complete message history.
        """
        return self.messages

    def get_agent_interactions(self, agent_name: str) -> List[Dict[str, str]]:
        """
        Get all messages related to a specific agent.
        """
        return [
            msg for msg in self.messages 
            if msg.get('sender') == agent_name or 
            agent_name in self._get_relevant_agents(
                self._analyze_message_content(msg['content']),
                None
            )
        ]