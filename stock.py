import streamlit as st
import yfinance as yf

# Set the page title
st.title("Stock Data App")

# Create a text input for the user to enter a stock symbol
stock_symbol = st.text_input("Enter a stock symbol:")

# Check if the user has entered a stock symbol
# Create a function to search for ticker information by company name
def search_ticker_by_name(company_name):
    # Use yfinance to search for ticker symbols based on company name
    ticker_symbols = yf.Tickers(company_name)

    # Get the first ticker symbol from the search results
    first_ticker_symbol = ticker_symbols.tickers[0].info['symbol']

    # Use yfinance to get the stock data for the first ticker symbol
    stock_data = yf.Ticker(first_ticker_symbol)

    # Get the stock information
    stock_info = stock_data.info

    # Display the stock information
    st.write("Stock Information:")
    st.write(stock_info)

# Create a text input for the user to enter a company name
company_name = st.text_input("Enter a company name:")

# Check if the user has entered a company name
if company_name:
    # Use yfinance to search for ticker symbols based on company name
    ticker_symbols = yf.Tickers(company_name)

    # Get the list of ticker symbols from the search results
    ticker_symbol_list = [ticker.ticker for ticker in ticker_symbols.tickers]

    # Display the search suggestions
    st.write("Search Suggestions:")
    st.write(ticker_symbol_list)

    # Check if there are any ticker symbols in the search results
    if ticker_symbol_list:
        # Create a selectbox for the user to choose a ticker symbol from the search results
        selected_ticker_symbol = st.selectbox("Select a ticker symbol:", ticker_symbol_list)

        # Check if the user has selected a ticker symbol
        if selected_ticker_symbol:
            # Use yfinance to get the stock data for the selected ticker symbol
            stock_data = yf.Ticker(selected_ticker_symbol)

            # Get the stock information
            stock_info = stock_data.info

            # Display the stock information
            st.write("Stock Information:")
            st.write(stock_info)
