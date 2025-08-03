from autogen_agentchat.agents import AssistantAgent
from config.constants import SYSTEM_MESSAGE

def create_agent(name, model, mcp_tools):

    agent = AssistantAgent(
        name=name,
        system_message=SYSTEM_MESSAGE,
        model_client=model,
        tools=mcp_tools,
        reflect_on_tool_use=True
    )

    return agent
