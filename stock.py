import streamlit as st
import yfinance as yf

# Set the page title
st.title("Stock Data App")

# Create a text input for the user to enter a stock symbol
stock_symbol = st.text_input("Enter a stock symbol:")

# Check if the user has entered a stock symbol
if stock_symbol:
    # Use yfinance to get the stock data
    stock_data = yf.Ticker(stock_symbol)

    # Get the stock information
    stock_info = stock_data.info

    # Display the stock information
    st.write("Stock Information:")
    st.write(stock_info)