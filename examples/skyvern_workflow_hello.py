import asyncio
from skyvern import Skyvern

async def run_visual_workflow():
    """
    Example of using Skyvern for vision-based browser automation (2026).
    Requires: pip install skyvern
    """
    async with Skyvern(api_key="YOUR_SKYVERN_API_KEY") as skyvern:
        print("--- Running Skyvern Visual Workflow ---")
        
        # Skyvern uses computer vision and LLMs to navigate and extract data
        result = await skyvern.run_task(
            prompt="Login to the simulated insurance portal, navigate to the claims section, and extract the status of the latest claim.",
            url="https://example-insurance-portal.com"
        )
        
        print(f"Workflow Result: {result}")

if __name__ == "__main__":
    asyncio.run(run_visual_workflow())
