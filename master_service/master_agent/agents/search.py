from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

class SearchAgent:
    def __init__(self) -> None:
        pass

    def search(self, ticker):
        query = f"Stock analysis for {ticker}"
        results = tavily_client.search(query=query, topic="news", max_results=10, include_images=True)
        sources = results["results"]
        return sources
    
    def run(self, data: dict):
        res = self.search(data["ticker"])
        data["sources"] = res
        return data
