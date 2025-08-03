from autogen_ext.tools.mcp import StdioServerParams


SYSTEM_MESSAGE = """
You are a helpful assistant that searches for hotels using the Airbnb data source. 
Use the Airbnb tool to fetch all hotel-related information. 

For storing, saving, or retrieving files and summaries, use the filesystem tool. 

Use the appropriate tool for each request, provide clear and concise results, and 
indicate "TERMINATE" when you have completed the task.
"""


AIRBNB_PARAMS = StdioServerParams(
        command="npx",
        args=[
            "-y",
            "@openbnb/mcp-server-airbnb",
            "--ignore-robots-txt"
        ],
        read_timeout_seconds=30
    )


FILESYSTEM_PARAMS = StdioServerParams(
        command="npx",
        args=[
            "-y",
            "@modelcontextprotocol/server-filesystem",
            "D:/Data Science/My Projects/MCP using AutoGen/output"
        ],
        read_timeout_seconds=30
    )



