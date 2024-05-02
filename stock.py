import yfinance as yf
import streamlit as sl
import pandas as pd
import difflib

start = sl.date_input('Start date', pd.to_datetime('2019-01-01'))
end = sl.date_input('End date', pd.to_datetime('today'))

def get_suggestions(search_input):
                suggestions = difflib.get_close_matches(search_input, ticker_dict.keys())
                return suggestions

def get_ticker_dict():
        df = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
        ticker_dict = dict(zip(df['Security'], df['Symbol']))
        return ticker_dict

ticker_dict = get_ticker_dict()

search_input = sl.text_input('Search by company name or symbol', key='search_input')

# Create a list of suggestions based on the search input
suggestions = get_suggestions(search_input)

# Display a dropdown of suggestions while typing
selected_suggestion = sl.selectbox('Suggestions', suggestions)

if selected_suggestion:
    symbol = ticker_dict[selected_suggestion]
    data = yf.download(symbol, start, end)
    if not data.empty:
        sl.write(f"Search result for '{selected_suggestion}':")
        sl.line_chart(data['Adj Close'])
        # Display graph for GSPC
        gspc_data = yf.download('^GSPC', start, end)
        if not gspc_data.empty:
            sl.write("S&P 500 (^GSPC):")
            sl.line_chart(gspc_data['Adj Close'])
        else:
            sl.write("No data found for GSPC")
    else:
        sl.write(f"No data found for '{selected_suggestion}'")



suggestions = get_suggestions(search_input)

def display_suggestions(suggestions):
                    if suggestions:
                        sl.write("Did you mean:")
                        for suggestion in suggestions:
                            if suggestion in ticker_dict.keys():
                                symbol = ticker_dict[suggestion]
                                data = yf.download(symbol, start, end)
                                if not data.empty:
                                    if sl.button(suggestion):
                                        sl.write(f"{suggestion}: {symbol}")
                                        sl.line_chart(data['Adj Close'])
                                else:
                                    sl.write(f"No data found for '{suggestion}'")

display_suggestions(suggestions)