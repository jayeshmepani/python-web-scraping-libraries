import asyncio
import os
from skyvern import Skyvern
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()

async def run_visual_workflow():
    """
    Example of using Skyvern for vision-based browser automation (2026).
    Requires: SKYVERN_API_KEY in your .env file.
    """
    api_key = os.getenv("SKYVERN_API_KEY", "YOUR_SKYVERN_API_KEY_HERE")
    
    async with Skyvern(api_key=api_key) as skyvern:
        print("--- Running Skyvern Visual Workflow ---")
        
        # Skyvern uses computer vision and LLMs to navigate and extract data.
        # This simulated prompt demonstrates the 2026 agentic capability.
        result = await skyvern.run_task(
            prompt="Extract the first visible quote and its author from the page.",
            url="https://quotes.toscrape.com"
        )
        
        print(f"Workflow Result: {result}")

if __name__ == "__main__":
    asyncio.run(run_visual_workflow())
