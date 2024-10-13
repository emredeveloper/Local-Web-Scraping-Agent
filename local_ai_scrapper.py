from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info

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