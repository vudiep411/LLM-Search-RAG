from langchain_community.llms import Ollama
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

"""
Before running this service, 
install Ollama on your local machine and pull the model you want 
to use. visit https://ollama.com/
"""

llm = Ollama(model="llama3.1")

app = FastAPI()

class Message(BaseModel):
    content: str

@app.post("/generate")
async def get_analysis(text: Message):
    res = llm.invoke(text.content)
    return {"content": res}
    