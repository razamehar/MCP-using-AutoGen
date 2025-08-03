# AI Assistant with MCP using AutoGen

An interactive AI assistant powered by **AutoGen**, **OpenAI**, and **Model Context Protocol (MCP)**. This assistant supports file system access, and web-based tasks using MCP agents.

This assistant uses **MCP servers** to interact with both:
- **Airbnb** (to search listings)
- **Local filesystem** (to read/write files)
---

## Features

- Conversational AI assistant
- Integrates AutoGen's `OpenAIChatCompletionClient` model  
- Uses MCP to interact with:
  - Airbnb website data
  - Local filesystem
- Can write responses to local files

---

## Tech Stack

- Python 3.10+
- AutoGen
- [OpenAI](https://platform.openai.com/)
- [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol)
- Node.js (for running MCP servers)
- Asyncio for non-blocking I/O

---

## Project Structure


## Setup Instructions
1. Clone the Repository
```bash
git clone https://github.com/razamehar/MCP-using-AutoGen.git
cd MCP-using-AutoGen
```

2. Install Node.js
Make sure Node.js is installed on your system. You can download it from nodejs.org.

3. Install Python Dependencies
```bash
pip install autogen_agentchat autogen_ext mcp openai tiktoken
```

4. Add .env File
```ini
OPENAI_API_KEY=your_openai_api_key
```
5. Run the Assistant
```bash
 python -m src.main
```

## MCP Configuration (browser_mcp.json)
This configuration enables two MCP servers:
- Airbnb MCP Server (for browsing listings)
- Filesystem MCP Server (for reading/writing local files)
Update the local path in the filesystem config to match your environment.

## Notes
- You must have Node.js installed to run MCP servers.
- This assistant supports memory through MCPAgent(memory_enabled=True).
- You can add more MCP servers to browser_mcp.json as needed.

## Contact

For any questions or clarifications, please contact Raza Mehar at [raza.mehar@gmail.com].