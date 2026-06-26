# 🕷️ Python Web Scraping Libraries (Ultimate 2026 Edition)

The undisputed **most complete** and up-to-date curated list of Python libraries for web scraping, data extraction, and autonomous AI agents. Fully synchronized for **April 20, 2026**.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Ultimate_Saturation_2026-success)](MAINTENANCE.md)
[![June 2026 Sync](https://img.shields.io/badge/Sync-June_26_2026-blueviolet)](requirements.txt)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## ⚙️ Installation & Architecture (Modular)

As of **April 2026**, the Python agentic ecosystem has evolved so rapidly that several state-of-the-art libraries have **mutually exclusive** dependency chains. To ensure stability, this toolkit uses a **Modular Architecture**.

### 1. The Core Stable Stack (100% Conflict-Free)
To install the foundational 40+ compatible libraries in a single environment:
```bash
pip install -r requirements.txt
```

### 2. The Modular AI/Agent Extensions
Install these in **isolated virtual environments** to avoid version conflicts (due to aiohttp, websockets, or anthropic pin incompatibilities):

| Stack | Installation Command | Key Tools Included |
| :--- | :--- | :--- |
| **Foundational Basics** | `pip install .[foundational]` | requests, scrapy, scrapy-redis, selenium, urllib3, extruct |
| **Agentic Alpha** | `pip install .[agentic-skyvern]` | Skyvern (Vision-Native) |
| **Agentic Beta** | `pip install .[agentic-browseruse]` | Browser-Use (LangChain Core) |
| **Automation Pro** | `pip install .[automation-pro]` | SeleniumBase (Stealth Pro) |
| **AI-PDF** | `pip install .[ai-pdf]` | Marker-PDF (LLM Extraction) |
| **Full AI Core** | `pip install .[ai-core,agentic-core]` | Crawl4AI, MultiOn, Stagehand |
| **Legacy Tools** | `pip install .[legacy]` | grab-site, cloudscraper |

---

## 📦 Ultimate Quick Selection Guide

| If you need to... | Recommended Stack |
| :--- | :--- |
| **Agentic Task Autonomy** | `stagehand`, `browser-use`, or `multion` |
| **Stealth & Bot Evasion** | `nodriver`, `curl_cffi`, or `camoufox` |
| **AI / RAG / Markdown** | `crawl4ai`, `firecrawl`, or `marker-pdf` |
| **Industrial Scaling** | `Scrapy` + `scrapy-redis` + `selectolax` |
| **Clean News & Articles** | `trafilatura` or `goose3` |
| **Finance & Ecommerce** | `price-parser` + `dateparser` |
| **Metadata & Structured RDF** | `extruct` |

---

## 🧩 Complete Library Manifest & Use Cases

### 1. Foundational & Classic HTML/XML Parsers
The building blocks of traditional web scraping. They are lightweight, fast, and ideal for static pages.

*   **requests**
    *   **Use Case:** The most human-friendly, standard library for making synchronous HTTP requests. Perfect for simple API calls and downloading static page HTML.
    *   **Install:** `pip install requests`
*   **beautifulsoup4** (bs4)
    *   **Use Case:** Easy-to-use parser for extracting data from HTML and XML. Ideal for beginners and small-scale scraping projects where developer speed matters more than raw parsing performance.
    *   **Install:** `pip install beautifulsoup4`
*   **lxml**
    *   **Use Case:** High-performance, low-level C-based binding for parsing XML and HTML. Supports full XPath 1.0 queries and CSS selectors with excellent speed.
    *   **Install:** `pip install lxml`
*   **selectolax**
    *   **Use Case:** Ultra-fast HTML parser utilizing the Modest/Lexbor rendering engines written in C. Hundreds of times faster than BeautifulSoup/lxml, perfect for high-throughput, CPU-bound parsing pipelines.
    *   **Install:** `pip install selectolax`
*   **urllib3**
    *   **Use Case:** A powerful, low-level HTTP client featuring thread-safe connection pooling, file post uploads, and robust request retrying.
    *   **Install:** `pip install urllib3`

### 2. Large-Scale & Industrial Frameworks
Engineered for scale, distributed crawling, and robust browser-based actions.

*   **Scrapy**
    *   **Use Case:** The premier asynchronous web crawling framework in Python. Built-in support for request scheduling, pipeline processing, item exporter, and concurrency.
    *   **Install:** `pip install Scrapy`
*   **scrapy-redis**
    *   **Use Case:** Redis-based scheduler and queue system for Scrapy. Enables horizontal scaling of spiders across multiple worker nodes.
    *   **Install:** `pip install scrapy-redis`
*   **selenium**
    *   **Use Case:** The historic standard for web automation. Emulates real user actions (clicks, keypresses, forms) on dynamic, JavaScript-heavy sites.
    *   **Install:** `pip install selenium`

### 3. Agentic & LLM-Driven Web Browsing
Modern frameworks that allow LLMs and vision models to steer the browser as an agent environment.

*   **Stagehand**
    *   **Use Case:** An AI-first agentic browser controller that enables natural-language-guided navigation, element interaction, and structured data extraction.
    *   **Install:** `pip install stagehand` (or `pip install .[agentic-core]`)
*   **browser-use**
    *   **Use Case:** An autonomous agent framework that empowers LLMs to interactively control a Chromium-based browser via LangChain.
    *   **Install:** `pip install browser-use` (or `pip install .[agentic-browseruse]`)
*   **multion**
    *   **Use Case:** API client for the MultiOn agent service. Allows agent systems to perform multi-step web tasks autonomously via remote API sessions.
    *   **Install:** `pip install multion` (or `pip install .[agentic-multion]`)
*   **skyvern**
    *   **Use Case:** Vision-native browser automation workflows. Uses LLMs and computer vision to navigate and extract data from unpredictable user interfaces without brittle XPath selectors.
    *   **Install:** `pip install skyvern` (or `pip install .[agentic-skyvern]`)
*   **kadoa-sdk** (Kadoa)
    *   **Use Case:** AI-powered extraction API designed to automatically parse messy websites and return pristine JSON schemas using vision intelligence.
    *   **Install:** `pip install kadoa-sdk` (or `pip install .[agentic-core]`)
*   **browserbase**
    *   **Use Case:** Python SDK to interact with Browserbase, a serverless platform running headless browsers at scale, offering proxy management, session logging, and stealth out-of-the-box.
    *   **Install:** `pip install browserbase` (or `pip install .[agentic-core]`)

### 4. AI-Native & RAG Extraction
Libraries optimized to ingest, structure, and convert messy web contents into LLM-ready markdown or schemas.

*   **crawl4ai**
    *   **Use Case:** Asynchronous web crawler built specifically for RAG (Retrieval-Augmented Generation) and LLMs. Converts raw webpages into clean Markdown, structured JSON, or text blocks.
    *   **Install:** `pip install crawl4ai` (or `pip install .[ai-core]`)
*   **firecrawl-py** (Firecrawl)
    *   **Use Case:** Python SDK for Firecrawl, a managed crawling service that parses any URL into LLM-compatible formats (Markdown, structured text).
    *   **Install:** `pip install firecrawl-py` (or `pip install .[ai-core]`)
*   **scrapegraphai**
    *   **Use Case:** A prompt-driven, graph-based scraping library. Feed it a prompt and a URL, and it leverages LLMs to generate the scraping code/graph dynamically.
    *   **Install:** `pip install scrapegraphai` (or `pip install .[ai-core]`)
*   **marker-pdf**
    *   **Use Case:** Converts PDF documents (and images) to clean Markdown. Excels at removing headers/footers, converting tables to markdown, and rendering math formulas with OCR.
    *   **Install:** `pip install marker-pdf` (or `pip install .[ai-pdf]`)
*   **goose3**
    *   **Use Case:** Article extractor that parses article body text, author list, publication dates, and primary images from blogs and news websites.
    *   **Install:** `pip install goose3` (or `pip install .[ai-core]`)

### 5. Modern Stealth & Anti-Bot Evasion
Tools designed to bypass advanced anti-scraping systems like Cloudflare, Akamai, and DataDome.

*   **nodriver**
    *   **Use Case:** An asynchronous framework to control Chrome/Chromium without standard WebDriver detection, bypassing modern anti-bot measures by interacting directly with the browser engine.
    *   **Install:** `pip install nodriver` (or `pip install .[stealth]`)
*   **curl_cffi**
    *   **Use Case:** An HTTP client that spoofs browser TLS fingerprints (JA3/JA4) and HTTP/2 settings, allowing you to bypass Cloudflare security walls when doing requests-based scraping.
    *   **Install:** `pip install curl_cffi` (or `pip install .[stealth]`)
*   **camoufox**
    *   **Use Case:** Anti-detect browser engine built on Firefox. Fingerprint-resistant out-of-the-box, it rotates fonts, screen sizes, graphics configs, and WebGL specs to hide automation indicators.
    *   **Install:** `pip install camoufox` (or `pip install .[stealth]`)
*   **seleniumbase**
    *   **Use Case:** All-in-one Selenium wrapper. Features "UC Mode" (Undetected-Chromedriver) to bypass CAPTCHAs, plus built-in visual regression testing capabilities.
    *   **Install:** `pip install seleniumbase` (or `pip install .[automation-pro]`)
*   **DrissionPage**
    *   **Use Case:** A unified browser and requests library. Lets you parse static HTML using fast requests-style parsing, and instantly transition to an automated browser when dynamic JS rendering is needed.
    *   **Install:** `pip install DrissionPage` (or `pip install .[stealth]`)
*   **playwright-stealth**
    *   **Use Case:** Stealth plugin to mask Playwright's automated browser footprint, preventing simple detection from security scripts.
    *   **Install:** `pip install playwright-stealth` (or `pip install .[stealth]`)
*   **undetected-chromedriver**
    *   **Use Case:** Patched Selenium ChromeDriver binary that does not trigger Google Chrome's automation flags. Great for standard Selenium tasks.
    *   **Install:** `pip install undetected-chromedriver` (or `pip install .[stealth]`)

### 6. Specialized & Domain Extractors
Targeted crawlers and specialized scrapers for multimedia, news, and complex metadata formats.

*   **yt-dlp**
    *   **Use Case:** High-fidelity video and audio downloader with support for metadata extraction, thumbnail downloading, and playlist scraping across thousands of websites.
    *   **Install:** `pip install yt-dlp` (or `pip install .[specialized]`)
*   **trafilatura**
    *   **Use Case:** High-quality article content scraper and text cleaner. Fast and lightweight; perfect for extracting structural texts from blogs, forums, and articles.
    *   **Install:** `pip install trafilatura` (or `pip install .[specialized]`)
*   **newspaper4k**
    *   **Use Case:** Active fork of the original `newspaper` news mining library. Allows multi-language news extraction, keyword extraction, and author parsing.
    *   **Install:** `pip install newspaper4k` (or `pip install .[specialized]`)
*   **pywebcopy**
    *   **Use Case:** Full website and assets copier. Clones a complete page along with its relative styles, scripts, and fonts locally.
    *   **Install:** `pip install pywebcopy` (or `pip install .[specialized]`)
*   **extruct**
    *   **Use Case:** Formatted metadata extractor. Parses semantic data like JSON-LD, Microdata, RDFa, Dublin Core, and OpenGraph markup from raw HTML.
    *   **Install:** `pip install extruct` (or `pip install .[foundational]`)

### 7. Data Cleaning, Parsing & Pipeline Utilities
Helper tools to clean and format scraped text, handle rate limits, and construct schema-conforming items.

*   **dateparser**
    *   **Use Case:** Parses localized, natural-language, or relative dates (e.g., "yesterday", "2 weeks ago", "hace 2 horas") into standard datetime objects.
    *   **Install:** `pip install dateparser` (or `pip install .[cleaning]`)
*   **price-parser**
    *   **Use Case:** Extracts numerical price values and currency symbols from dirty e-commerce product texts.
    *   **Install:** `pip install price-parser` (or `pip install .[cleaning]`)
*   **tenacity**
    *   **Use Case:** General-purpose retrying library with exponential backoff, jitter, and decorator syntax to make API and web requests resilient.
    *   **Install:** `pip install tenacity` (or `pip install .[cleaning]`)
*   **fake-useragent**
    *   **Use Case:** Programmatically generates random, valid browser user-agent headers updated based on actual usage statistics.
    *   **Install:** `pip install fake-useragent` (or `pip install .[cleaning]`)
*   **pydantic**
    *   **Use Case:** Data validation and parsing using Python type annotations. Ideal for structuring scraped outputs into reliable, type-safe JSON objects.
    *   **Install:** `pip install pydantic`
*   **python-dotenv**
    *   **Use Case:** Loads environment configurations from `.env` files. Essential for managing private keys, user names, and API keys securely.
    *   **Install:** `pip install python-dotenv`

### 8. Legacy & Auxiliary Tools
Maintained for archive compatibility or reference under historical stacks.

*   **grab-site**
    *   **Use Case:** Specialized web archiver crawler designed to crawl and backup entire websites as standardized WARC files. *(Requires Python <3.13)*
    *   **Install:** `pip install grab-site` (or `pip install .[legacy]`)
*   **cloudscraper**
    *   **Use Case:** A legacy client designed to bypass older Cloudflare anti-bot verification page challenges. *(Unmaintained; kept for historical reference)*
    *   **Install:** `pip install cloudscraper` (or `pip install .[legacy]`)

---

## 🏗️ Project Architecture

*   **[requirements.txt](requirements.txt)**: Core compatible libraries verified for Python 3.10–3.13.
*   **[MAINTENANCE.md](MAINTENANCE.md)**: Real-time health logs and certification statuses.
*   **[examples/](examples/)**: "Hello World" boilerplate templates to kickstart scraping projects:
    *   [requests_bs4_hello.py](examples/requests_bs4_hello.py)
    *   [playwright_hello.py](examples/playwright_hello.py)
    *   [crawl4ai_hello.py](examples/crawl4ai_hello.py)
    *   [browserbase_playwright_hello.py](examples/browserbase_playwright_hello.py)
    *   [skyvern_workflow_hello.py](examples/skyvern_workflow_hello.py)
    *   [agentic_multion_hello.py](examples/agentic_multion_hello.py)

---

## 🤝 Contributing

The ultimate list is never finished. Check [CONTRIBUTING.md](CONTRIBUTING.md) and join the ecosystem!

---
**Maintained by [Jayesh Mepani](https://jayeshmepani.site/)**  
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-flat&logo=github&logoColor=white)](https://github.com/jayeshmepani)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/jayeshmepani)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-flat&logo=gmail&logoColor=white)](mailto:jayeshmepani777@gmail.com)
