import sys
import asyncio

# Fix for Windows event loop closed RuntimeError
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from autogen_ext.tools.mcp import mcp_server_tools
from src.models.model_loader import load_model
from src.agents.agent_factory import create_agent
from src.teams.team_factory import create_team
from config.constants import AIRBNB_PARAMS, FILESYSTEM_PARAMS


async def config():
    model = load_model()

    airbnb_mcp_tools = await mcp_server_tools(server_params=AIRBNB_PARAMS)
    file_mcp_tools = await mcp_server_tools(server_params=FILESYSTEM_PARAMS)

    airbnb_agent = create_agent("airbnb_agent", model, airbnb_mcp_tools)
    file_agent = create_agent("file_agent", model, file_mcp_tools)
    agents = [airbnb_agent, file_agent]

    team = create_team(agents)
    return team


def print_message(msg):
    try:
        # If content is plain text
        if hasattr(msg, "content") and isinstance(msg.content, str):
            print(msg.content.strip())

        elif isinstance(msg, list):
            for item in msg[:3]:
                title = item.get('title', '')
                price = item.get('price', '')
                rating = item.get('rating', '')
                url = item.get('url', '')
                print(f"{title}\nPrice: {price}\nRating: {rating}\nURL: {url}\n")

    except Exception as e:
        pass  # Optional: silence noisy errors, or log to a file


async def orchestrate(team, task):
    async for msg in team.run_stream(task=task):
        yield msg


async def main():
    team = await config()
    task = "Search for hotels in Barcelona and save the summarized results as a text file in the output directory."


    async for msg in orchestrate(team, task):
        print_message(msg)

    if hasattr(team, "close"):
        await team.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "Event loop is closed" not in str(e):
            raise
