# tests/test_communication_manager.py

import pytest
from unittest.mock import Mock, patch
from agentx.communication_manager import CommunicationManager, TopicCategory
from agentx.providers.openai_provider import OpenAIProvider
from agentx.ai_agent import AIAgent

@pytest.fixture
def mock_ai_provider():
    provider = Mock(spec=OpenAIProvider)
    provider.generate_response.return_value = "Test response"
    return provider

@pytest.fixture
def mock_agent():
    agent = Mock(spec=AIAgent)
    agent.name = "Test Agent"
    return agent

@pytest.fixture
def communication_manager(mock_ai_provider):
    return CommunicationManager(agents=[], ai_provider=mock_ai_provider)

def test_analyze_message_content(communication_manager):
    # Test business-related content
    business_message = "We need to analyze the ROI of this project"
    topics = communication_manager._analyze_message_content(business_message)
    assert TopicCategory.BUSINESS in topics

def test_analyze_message_content_technical(communication_manager):
    # Test technical content
    tech_message = "The API integration needs to be implemented"
    topics = communication_manager._analyze_message_content(tech_message)
    assert TopicCategory.TECHNICAL in topics

def test_empty_message_content(communication_manager):
    # Test empty content
    empty_message = ""
    topics = communication_manager._analyze_message_content(empty_message)
    assert len(topics) == 0

@patch('agentx.communication_manager.CommunicationManager._ai_analyze_content')
def test_ai_fallback_analysis(mock_ai_analyze, communication_manager):
    mock_ai_analyze.return_value = {TopicCategory.BUSINESS}
    message = "This is a very ambiguous message"
    topics = communication_manager._analyze_message_content(message)
    assert mock_ai_analyze.called
    assert TopicCategory.BUSINESS in topics