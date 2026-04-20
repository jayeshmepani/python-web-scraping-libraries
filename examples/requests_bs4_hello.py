import requests
from bs4 import BeautifulSoup

def scrape_example():
    """
    A simple example of fetching a page with requests and parsing it with BeautifulSoup.
    """
    url = "https://example.com"
    print(f"--- Scraping {url} ---")
    
    try:
        # 1. Fetch the HTML
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Check for HTTP errors
        
        # 2. Parse the HTML
        soup = BeautifulSoup(response.text, 'lxml')
        
        # 3. Extract data
        title = soup.find('h1')
        paragraph = soup.find('p')
        
        print(f"Title: {title.get_text() if title else 'N/A'}")
        print(f"Content: {paragraph.get_text() if paragraph else 'N/A'}")
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_example()
