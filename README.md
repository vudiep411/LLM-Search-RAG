# 📈 Stock Ticker Analysis Application
This application is designed to provide a comprehensive analysis of a given stock ticker. The workflow involves checking the current price of the ticker, searching for relevant articles, filtering for the most relevant articles, and generating a summary report with sentiment analysis. The application is built using FastAPI and Ngrok to run and expose the API endpoint.

https://github.com/user-attachments/assets/c13e3b4d-93fe-477e-9d77-06d78b7fc129

## 🌟 Table of Contents
- [📈 Stock Ticker Analysis Application](#-stock-ticker-analysis-application)
  - [🌟 Table of Contents](#-table-of-contents)
  - [🚀 Installation](#-installation)
    - [LLM API](#llm-api)
    - [Master Service](#master-service)
    - [Frontend](#frontend)
  - [🛠️ Architecture](#️-architecture)
  - [🔍 API Services](#-api-services)
    - [LLM Service](#llm-service)
      - [Usage](#usage)
    - [Analysis/Master Service](#analysismaster-service)
      - [Usage](#usage-1)
  - [⚙️ Workflow](#️-workflow)
  - [📃 License](#-license)

## 🚀 Installation
### LLM API
This is a self hosted LLM model locally using Ollama. The model I will be using is llama3
> **Prerequisite**: *[Ollama](https://ollama.com/) installed on your machine*
```
ollama run llama3
```
Step 1: Install dependencies
```
cd llm_service
pip install -r requirements.txt
```

Step 2: Run scripts to start the fastapi server:
> Linux
```
./script.sh
```

> Window
```
./script.bat
```
* Server will run on localhost:8001

### Master Service
This is the main API for the stock analysis utilizing search engine Tavily and our own LLM API in LLM service

Configure environment variable [.env.example](.env.example)
```
TAVILY_API_KEY=""
STOCK_API_KEY=""
LLM_SERVICE_URL=http://127.0.0.1:8001
```
> Visit [twelveapi](https://twelvedata.com/) for the **STOCK_API_KEY**

> Visit [Tavily](https://tavily.com/) for **TAVILY_API_KEY**
> 
Step 1: Install dependencies
```
cd master_agent
pip install -r requirements.txt
```
Step 2: Run scripts to start the fastapi server:
> Linux
```
./script.sh
```

> Window
```
./script.bat
```
* Server will run on localhost:8000

### Frontend
I use streamlit for a quick prototype for this application.
Step 1: Install dependencies
```
cd frontend
pip install -r requirements.txt
```
Step 2: Run scripts to start the fastapi server:
> Linux
```
./script.sh
```

> Window
```
./script.bat
```

## 🛠️ Architecture
1. **Price Agent**: Use Twelve API to retrieve the current stock price
2. **Search**: Search for relevant articles for analysis
3. **Filter Agent**: Filter the article by score based on search results
4. **LLM Agent**: Use RAG technique with self-hosted llama3 model for sentiment analysis

   <img src="/documents/architecture.png"/>

## 🔍 API Services
### LLM Service
The Text Analysis API allows users to send a text message and receive a generated analysis based on the llama3 model from Ollama.
#### Usage
```bash
curl -X POST "http://127.0.0.1:8001/generate" -H "Content-Type: application/json" -d '{"content": "Analyze this text"}'
```
```python
import requests
url = "http://127.0.0.1:8001/generate"
res = requests.post(url, json={"content": "Hi, how are you today?"})
```
### Analysis/Master Service
Run the workflow to retrieve the stock analysis utilizing the llama3 service and RAG technique

#### Usage
```bash
curl -X 'GET' \
  'http://example.com/ticker?ticker=AAPL' \
  -H 'accept: application/json'
```
```python
import requests

url = 'http://127.0.0.1:8000/ticker'
params = {'ticker': 'AAPL'}
headers = {'accept': 'application/json'}

response = requests.get(url, params=params, headers=headers)
data = response.json()

print(data)
```

## ⚙️ Workflow
1. User Input:
    * The user provides a stock ticker.
2. Price Agent:
   * The application checks the current price of the ticker.
If the ticker does not exist, the application returns an error and ends the process.

3. Search Agent:
    * If the ticker exists, the application searches for articles and sources related to the stock ticker.

4. Article Filtering:
   * The articles are filtered based on the score from Tavily search tool
  
5. Summary Report:
   * The most relevant article is then passed into the LLM again to write a summary report and sentiment analysis.
   * The summary report is returned to the user.

## 📃 License
This project is licensed under the MIT License.
