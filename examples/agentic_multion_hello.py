import multion

def agent_browse():
    """
    Example of using the MultiOn API (2026 version) for autonomous browsing.
    Requires: pip install multion
    """
    print("--- Starting MultiOn Agentic Browser ---")
    
    # This command allows the agent to decide which sites to visit and how to interact
    response = multion.browse(
        cmd="Find the latest stock price of NVIDIA and summarized the top 3 news stories about it.",
        url="https://www.google.com" # Starting point
    )
    
    # The response contains the final summarized data and the status of the agent's task
    print(f"Agent Response: {response}")

if __name__ == "__main__":
    agent_browse()
