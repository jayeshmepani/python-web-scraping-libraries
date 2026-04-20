import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    """
    Example of using Crawl4AI to fetch a site and get clean Markdown.
    Note: Requires 'crawl4ai' package.
    """
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url="https://example.com")
        
        print("--- Crawl4AI Clean Markdown ---")
        # Crawl4AI provides the content in various formats (markdown, clean_html, etc)
        print(result.markdown[:500] + "...") # Print first 500 characters

if __name__ == "__main__":
    asyncio.run(main())
