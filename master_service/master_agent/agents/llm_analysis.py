from dotenv import load_dotenv
import os
import requests

class AnalysisPrompt:
    def __init__(self, current_price, sources, ticker) -> None:
        format_sources = ""
        url_site = []
        for i, source in enumerate(sources):
            format_sources += f"Source {i}: {source["url"]}\n Content: {source["content"]} \n"
            url_site.append(source["url"])

        self.prompt = """
            You are a financial analyst specializing in stock market analysis. You are tasked with summarizing and analyzing a specific stock and providing a sentiment analysis based on given sources. 
            Cite the source after the sentence in markdown format. eg. [source](url). Make sure the generated response is in markdown format so double check all special tokens.

            stock symbol: {ticker}
            url to site sources: {url_site}
            {sources}
            Current Price is {current_price}

            **Example Format Response:**
            ---
            ## Stock Summary and Analysis:

            - **Current Price:** $
            - **Company Overview:** XYZ is a leading provider of [products/services], operating primarily in [industry/sector]. Recently, the company has [recent significant events]. [source][url]
            - **Financial Performance:** The company reported a revenue of \$X million in the last quarter, with a profit margin of Y%. EPS was \$Z, showing an increase/decrease compared to the previous quarter. [source][url]
            - **Market Trends:** The [industry/sector] is currently experiencing [describe relevant trends]. [brief analysis]. Regulatory changes such as [regulatory factors] may impact the company. [source][url]
            - **Analyst Ratings:** Analysts have given the stock a rating of [rating], with a price target range of \$[low] to \$[high]. [source][url]

            **Sentiment Analysis:**

            - **Positive Sentiments:** [Summary of positive sentiments]
            - **Negative Sentiments:** [Summary of negative sentiments]
            - **Neutral Sentiments:** [Summary of neutral sentiments]

            **Conclusion:**

            - **Overall Sentiment:** The overall sentiment towards XYZ is [positive/negative/neutral].
            - **Investment Recommendation:** Based on the analysis, it is recommended to [buy/hold/sell] the stock. This recommendation is supported by [key points from the analysis].

            > Note: The above analysis is based on publicly available information and should not be taken as personalized investment advice.
        """.format(ticker=ticker, sources=format_sources, current_price=current_price, url_site=url_site)

    def __str__(self) -> str:
        return self.prompt
    

load_dotenv()
LLM_SERVICE_URL = os.getenv("LLM_SERVICE_URL")

class AnalysisAgent:
    def __init__(self) -> None:
        pass

    def get_analysis(self, ticker, sources, current_price):
        prompt = AnalysisPrompt(
            ticker=ticker,
            current_price=current_price,
            sources=sources
        )
        res = requests.post(LLM_SERVICE_URL + "/generate", json={"content": prompt.prompt})
        analysis = res.json()
        return analysis["content"]
    
    def run(self, data: dict):
        analysis = self.get_analysis(
            ticker=data["ticker"],
            sources=data["sources"],
            current_price=data["price"]
        )
        data["analysis"] = analysis
        return data