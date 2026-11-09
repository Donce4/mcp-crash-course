import asyncio
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_ollama import ChatOllama
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatOllama(model=os.getenv("OLLAMA_MODEL"))

stdio_server_params = StdioServerParameters(
    command = "python", 
    args=["/home/donce/Projects/mcp-crash-course/servers/math_server.py"]
)

async def main() -> None:
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
    asyncio.run(main())
