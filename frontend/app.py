import streamlit as st
import requests

MASTER_SERVICE="http://127.0.0.1:8000"

def get_stock_analysis(ticker):
    res = requests.get(f"{MASTER_SERVICE}/ticker?ticker={ticker}")
    data = res.json()
    data["analysis"] = data["analysis"].replace('$', '\\$')
    return data

st.set_page_config(page_title="Stock Analysis and Sentiment", page_icon="📈", layout="centered")

st.markdown("""
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stTextInput > div > div > input {
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    .css-1v0mbdj.etr89bj0 {
        border: none;
    }
    .main .block-container {
        max-width: 800px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📈 Stock Analysis and Sentiment")
st.write("Enter a stock ticker symbol to get the latest analysis and sentiment overview.")

ticker = st.text_input("Enter Stock Ticker", "", max_chars=10)

if st.button("Get Analysis"):
    if ticker:
        with st.spinner("Fetching data..."):
            data = get_stock_analysis(ticker)
        if data["error"]:
            st.error("Symbol does not exist")
        else:
            st.markdown(data["analysis"])
    else:
        st.error("Please enter a stock ticker.")