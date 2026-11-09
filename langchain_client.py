import asyncio
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_ollama import ChatOllama

load_dotenv()

llm = ChatOllama(model=os.getenv("OLLAMA_MODEL"))


async def main():
    print("Hello langchain mcp")


if __name__ == "__main__":
    asyncio.run(main())
