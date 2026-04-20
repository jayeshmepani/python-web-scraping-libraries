import os
from playwright.sync_api import sync_playwright
from browserbase import Browserbase

def run_serverless_browser():
    """
    Example of connecting Playwright to a serverless Browserbase session (2026).
    Requires: pip install browserbase playwright
    """
    bb = Browserbase(api_key="BROWSERBASE_API_KEY")
    
    # 1. Create a remote browser session
    print("--- Creating Serverless Browser Session ---")
    session = bb.sessions.create()
    
    # 2. Connect Playwright to the remote session over CDP
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(session.connect_url)
        # Use the existing page or create a new one
        page = browser.contexts[0].pages[0] if browser.contexts[0].pages else browser.new_page()
        
        print(f"--- Navigating remotely in Browserbase ---")
        page.goto("https://news.ycombinator.com/")
        
        print(f"Page Title: {page.title()}")
        browser.close()

if __name__ == "__main__":
    run_serverless_browser()
