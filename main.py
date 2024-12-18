# main.py

import logging
from providers.openai_provider import OpenAIProvider
from communication_manager import CommunicationManager
from agents.business_analyst_agent import BusinessAnalystAgent
from agents.it_consultant_agent import ITConsultantAgent
from agents.solution_architect_agent import SolutionArchitectAgent
from agents.project_manager_agent import ProjectManagerAgent
from agents.devops_lead_agent import DevOpsLeadAgent
from agents.tech_lead_agent import TechLeadAgent
from agents.markdown_output_agent import MarkdownOutputAgent

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("ai_consultancy.log"),
            logging.StreamHandler()
        ]
    )

def main():
    setup_logging()
    logging.info("Starting AI Consultancy Agents")

    # Initialize AI provider
    ai_provider = OpenAIProvider()  # Or GeminiProvider()

    # Initialize agents
    agents = [
        BusinessAnalystAgent(ai_provider=ai_provider),
        ITConsultantAgent(ai_provider=ai_provider),
        SolutionArchitectAgent(ai_provider=ai_provider),
        ProjectManagerAgent(ai_provider=ai_provider),
        DevOpsLeadAgent(ai_provider=ai_provider),
        TechLeadAgent(ai_provider=ai_provider),
    ]

    # Communication facilitator agent (could be the CommunicationManager)
    communication_manager = CommunicationManager(agents=agents)

    # Client input
    client_input = (
        "We are facing issues with data security and need to improve our system's scalability."
    )
    logging.info(f"Client input: {client_input}")

    # Agents process and communicate
    # Business Analyst
    ba_agent = next(agent for agent in agents if agent.name == "AI Business Analyst")
    ba_response = ba_agent.get_response(client_input)
    communication_manager.broadcast_message(ba_agent, ba_response)

    # IT Consultant
    it_agent = next(agent for agent in agents if agent.name == "AI IT Consultant")
    it_response = it_agent.get_response()
    communication_manager.broadcast_message(it_agent, it_response)

    # Solution Architect
    sa_agent = next(agent for agent in agents if agent.name == "AI Solution Architect")
    sa_response = sa_agent.get_response()
    communication_manager.broadcast_message(sa_agent, sa_response)

    # Tech Lead
    tech_lead_agent = next(agent for agent in agents if agent.name == "AI Tech Lead")
    tech_lead_response = tech_lead_agent.get_response()
    communication_manager.broadcast_message(tech_lead_agent, tech_lead_response)

    # DevOps Lead
    devops_lead_agent = next(agent for agent in agents if agent.name == "AI DevOps Lead")
    devops_response = devops_lead_agent.get_response()
    communication_manager.broadcast_message(devops_lead_agent, devops_response)

    # Project Manager
    pm_agent = next(agent for agent in agents if agent.name == "AI Project Manager")
    pm_response = pm_agent.get_response()
    communication_manager.broadcast_message(pm_agent, pm_response)

    # Compile responses
    aggregated_content = communication_manager.review_and_collate_responses()

    # Markdown Output Agent
    md_output_agent = MarkdownOutputAgent(ai_provider=ai_provider)
    final_output = md_output_agent.get_response(aggregated_content)

    # Output the final Markdown document
    with open("final_report.md", "w") as f:
        f.write(final_output)

    print("\n--- Final Report Generated ---")
    print(final_output)

    logging.info("AI Consultancy Agents interaction completed.")

if __name__ == "__main__":
    main()