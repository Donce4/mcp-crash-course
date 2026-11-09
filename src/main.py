import asyncio
from dotenv import load_dotenv
import os
load_dotenv()

print(os.getenv("OLLAMA_MODEL"))

async def main() -> None:
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
    asyncio.run(main())