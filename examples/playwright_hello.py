import asyncio
from playwright.async_api import async_playwright

async def scrape_dynamic_page():
    """
    A simple example of using Playwright to scrape a dynamic page.
    """
    async with async_playwright() as p:
        # Launch the browser
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        url = "https://quotes.toscrape.com"
        print(f"--- Browsing {url} with Playwright ---")
        
        # Navigate to the page
        await page.goto(url)
        
        # Wait for a specific element (useful for JS-heavy sites)
        await page.wait_for_selector("h1")
        
        # Extract data
        title = await page.inner_text("h1")
        print(f"Page Title: {title}")
        
        # Close the browser
        await browser.close()

if __name__ == "__main__":
    asyncio.run(scrape_dynamic_page())
