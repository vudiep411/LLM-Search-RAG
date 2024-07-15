# Stock Ticker Analysis Application
This application is designed to provide a comprehensive analysis of a given stock ticker. The workflow involves checking the current price of the ticker, searching for relevant articles, filtering for the most relevant articles, and generating a summary report with sentiment analysis. The application is built using FastAPI and Ngrok to run and expose the API endpoint.

## Table of Contents
- [Stock Ticker Analysis Application](#stock-ticker-analysis-application)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Architechture](#architechture)
  - [API Endpoint](#api-endpoint)
  - [Workflow](#workflow)
  - [License](#license)

## Installation
...
## Architechture
...

## API Endpoint
...

## Workflow
1. User Input:
    * The user provides a stock ticker.
2. Price Agent:
   * The application checks the current price of the ticker.
If the ticker does not exist, the application returns an error and ends the process.

3. Search Agent:
    * If the ticker exists, the application searches for articles and sources related to the stock ticker.

4. Article Filtering:
   * The articles are passed into a language model (LLM) to filter for the most relevant article.
  
5. Summary Report:
   * The most relevant article is then passed into the LLM again to write a summary report and sentiment analysis.
   * The summary report is returned to the user.

## License
This project is licensed under the MIT License.