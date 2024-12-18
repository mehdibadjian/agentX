# tests/test_communication_manager.py

import pytest
from communication_manager import CommunicationManager, TopicCategory
from providers.openai_provider import OpenAIProvider

def test_analyze_message_content():
    ai_provider = OpenAIProvider()
    comm_manager = CommunicationManager(agents=[], ai_provider=ai_provider)

    # Test business-related content
    business_message = "We need to analyze the ROI of this project"
    topics = comm_manager._analyze_message_content(business_message)
    assert TopicCategory.BUSINESS in topics

    # Test technical content
    tech_message = "The API integration needs to be implemented"
    topics = comm_manager._analyze_message_content(tech_message)
    assert TopicCategory.TECHNICAL in topics

def test_get_relevant_agents():
    ai_provider = OpenAIProvider()
    comm_manager = CommunicationManager(agents=[], ai_provider=ai_provider)

    # Add more specific tests based on your implementation
    assert True  # Placeholder assertion

# Add more test cases as needed