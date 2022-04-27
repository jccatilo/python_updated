import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock Price Application - jcac using streamlit.io and ngrok hehe.
nice.
""")

symbol = 'AAPL'
data = yf.Ticker(symbol)
df = data.history(period='1', start = '2012-12-12', end="2021-12-12")

st.write("""
## Closing Price
""")
st.line_chart(df.Close)

st.write("""
## Volume
""")
st.line_chart(df.Volume)