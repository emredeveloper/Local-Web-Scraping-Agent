from smart_scraper_graph import SmartScraperGraph

# Define the prompt, source, and configuration
prompt = "List me all the attractions in Chioggia."
source = "https://en.wikipedia.org/wiki/Chioggia"
config = {
    "llm": {"model": "gpt-3.5-turbo"}
}

# Create the smart scraper graph
smart_scraper = SmartScraperGraph(prompt, source, config)

# Run the smart scraper graph
result = smart_scraper.run()

print(result)