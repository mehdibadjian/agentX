**[in dev/testing phase]**

# AI-Driven IT Consultancy System

An advanced AI-powered system that simulates an IT consultancy firm using multiple specialized AI agents. The system leverages various AI models to provide comprehensive IT solutions, from business analysis to technical implementation planning.

## 📋 Table of Contents

- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [AI Agents](#-ai-agents)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

## 🚀 Features

- **Multi-Agent System**: Coordinated AI agents with specialized roles
- **AI Provider Agnostic**: Support for multiple AI providers (OpenAI, Gemini)
- **Intelligent Communication**: Inter-agent message review and coordination
- **Markdown Output**: Professional documentation generation
- **Secure Configuration**: Environment-based secure credential management
- **Extensive Logging**: Comprehensive logging system for debugging and monitoring

## 🏗 System Architecture

### Core Components

1. **Base Agent Framework**
   - Abstract AI agent implementation
   - Message handling system
   - Response generation pipeline

2. **Specialized Agents**
   - Business Analyst
   - IT Consultant
   - Solution Architect
   - Project Manager
   - DevOps Lead
   - Tech Lead
   - Markdown Output Agent

3. **Communication System**
   - Message broadcasting
   - Response review mechanism
   - Content aggregation

4. **AI Provider Interface**
   - Abstract provider interface
   - Concrete implementations (OpenAI, Gemini)
   - Easy extension for new providers

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- OpenAI API key or other supported AI provider credentials
- Virtual environment (recommended)

## 🔧 Installation

1. **Clone the Repository**
   ```bash
   git clone 
   cd ai-consultancy-system



Create and Activate Virtual Environment
# On Windows
python -m venv env
.\env\Scripts\activate

# On macOS/Linux
python3 -m venv env
source env/bin/activate



Install Dependencies
pip install -r requirements.txt



Set Up Environment Variables
cp .env.example .env
# Edit .env with your API keys and configuration



⚙️ Configuration
Environment Variables
Create a .env file in the project root:
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Gemini Configuration (if applicable)
GEMINI_API_KEY=your_gemini_api_key_here

# Logging Configuration
LOG_LEVEL=INFO

AI Provider Configuration
Modify config.py to adjust AI provider settings:
AI_PROVIDER_CONFIG = {
    "default_provider": "openai",
    "models": {
        "gpt-4": {"temperature": 0.7},
        "gpt-3.5-turbo": {"temperature": 0.5}
    }
}

🎯 Usage
Basic Usage


Start the System
python main.py



Provide Input
# The system will prompt for client requirements
Enter client requirements: We need to improve our system's scalability...



View Output

Check final_report.md for the comprehensive response
Review ai_consultancy.log for detailed system logs



Advanced Usage
Custom Agent Configuration
from agents import CustomAgent
from providers import OpenAIProvider

custom_agent = CustomAgent(
    name="Custom Agent",
    role_description="Specialized role",
    responsibilities=["Task 1", "Task 2"],
    model="gpt-4",
    ai_provider=OpenAIProvider()
)

🤖 AI Agents
Business Analyst Agent

Requirements gathering
Business process documentation
Needs analysis

IT Consultant Agent

Technical assessment
Solution recommendation
Strategic planning

Solution Architect Agent

System design
Technology selection
Architecture planning

Project Manager Agent

Project coordination
Timeline management
Resource allocation

DevOps Lead Agent

CI/CD pipeline design
Infrastructure automation
System reliability

Tech Lead Agent

Technical leadership
Code quality assurance
Development coordination

Markdown Output Agent

Documentation formatting
Report generation
Content organization

🤝 Contributing
We welcome contributions! Please follow these steps:

Fork the repository
Create a feature branch
git checkout -b feature/AmazingFeature


Commit changes
git commit -m 'Add AmazingFeature'


Push to branch
git push origin feature/AmazingFeature


Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

OpenAI for their GPT models
Google for Gemini (if applicable)
Contributors and maintainers
Open source community

📊 Project Status

 Basic agent framework
 OpenAI integration
 Inter-agent communication
 Markdown output
 Gemini integration
 Web interface
 API endpoints
 Docker support

🔍 Troubleshooting
Common Issues


API Key Issues
Error: OpenAI API key not found
Solution: Ensure OPENAI_API_KEY is set in .env



Dependencies
Error: Module not found
Solution: Run pip install -r requirements.txt



📚 Documentation
Detailed documentation is available in the docs/ directory:

docs/installation.md: Detailed installation guide
docs/configuration.md: Configuration options
docs/api.md: API documentation
docs/agents.md: Agent specifications

🔄 Updates and Versioning
We use SemVer for versioning. For available versions, see the tags on this repository.
📧 Contact
Your Name - @yourtwitter - email@example.com
Project Link: https://github.com/yourusername/ai-consultancy-system
🔮 Future Plans

Integration with more AI providers
Web-based user interface
Real-time collaboration features
API endpoint implementation
Docker containerization
Cloud deployment support


Made with ❤️ by Mehdi Badjian

