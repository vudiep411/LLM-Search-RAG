from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from master_agent.langgraph_agent import MasterAgent

app = FastAPI()

class WebHook(BaseModel):
    url: str

@app.get("/ticker")
async def get_analysis(ticker: str = Query(..., title="ticker", description="Get a stock analysis")):
    master_agent = MasterAgent(ticker)
    data = master_agent.run()
    res = {
        "ticker": data["ticker"],
        "price": data["price"],
        "error": True if data["price"] < 0 else False,
        "sources": data.get("sources", []),
        "analysis": data.get("analysis", "")
    } 
    return res

