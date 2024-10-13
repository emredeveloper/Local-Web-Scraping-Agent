# 🕵️‍♂️ Web Scraping AI Agent

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)
![scrapegraphai](https://img.shields.io/badge/scrapegraphai-latest-green)
![Playwright](https://img.shields.io/badge/Playwright-latest-orange)

An intelligent web scraping tool powered by AI, built with Streamlit and scrapegraphai. 🚀

## 📖 Description

This Web Scraping AI Agent allows you to extract information from websites using natural language prompts. It leverages the power of large language models (like GPT-3.5 and GPT-4) to understand your requests and return relevant data from web pages.

## 🌟 Features

- 🔍 AI-powered web scraping
- 💬 Natural language prompts for data extraction
- 🌐 Support for various websites
- 🤖 Integration with OpenAI's GPT models
- 🖥️ User-friendly Streamlit interface

## 🛠️ Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/web-scraping-ai-agent.git
   cd web-scraping-ai-agent
   ```

2. Install the required packages:
   ```
   pip install streamlit scrapegraphai playwright
   ```

3. Install Playwright browsers:
   ```
   playwright install
   ```

## 🚀 Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to the provided local URL (usually `http://localhost:8501`).

3. Enter your OpenAI API key.

4. Choose the AI model (GPT-3.5-turbo or GPT-4).

5. Enter the URL of the website you want to scrape.

6. Provide a natural language prompt describing what information you want to extract.

7. Click "Scrape" and wait for the results!

## 📊 Example

```python
from scrapegraphai.graphs import SmartScraperGraph

graph_config = {
    "llm": {
        "model": "ollama/llama3.2:3b",
        "temperature": 0,
        "format": "json",
        "base_url":"127.0.0.1:11434"
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text:v1.5",
        "temperature": 0,
    },
    "verbose": True,
}

smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the titles",
    source="https://www.wired.com/",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/web-scraping-ai-agent/issues).

## 📜 License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [scrapegraphai](https://github.com/username/scrapegraphai)
- [Playwright](https://playwright.dev/)
- [OpenAI](https://openai.com/)

---

Made with ❤️ and ☕
