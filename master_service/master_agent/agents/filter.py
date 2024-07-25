class FilterAgent:
    def __init__(self) -> None:
        pass

    def filter_source(self, ticker, sources):
        sources.sort(key=lambda x: x["score"], reverse=True)
        return [{"url": source["url"], "content": source["content"] }for source in sources[:6]]

    def run(self, data):
        filtered_source = self.filter_source(data["ticker"], data["sources"])
        data["sources"] = filtered_source
        return data