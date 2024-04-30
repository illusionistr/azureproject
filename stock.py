import yfinance as yf
import streamlit as sl
import pandas as pd
import difflib

start = sl.date_input('Start date', pd.to_datetime('2019-01-01'))
end = sl.date_input('End date', pd.to_datetime('today'))

def get_ticker_dict():
        df = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
        ticker_dict = dict(zip(df['Security'], df['Symbol']))
        return ticker_dict

ticker_dict = get_ticker_dict()

search_input = sl.text_input('Search by company name or symbol')
if search_input:
    if search_input in ticker_dict.values():
        # Search by symbol
        symbol = search_input
    elif search_input in ticker_dict.keys():
        # Search by company name
        symbol = ticker_dict[search_input]
    else:
        sl.write(f"No search result found for '{search_input}'")
        symbol = None

    if symbol:
        data = yf.download(symbol, start, end)
        if not data.empty:
            sl.write(f"Search result for '{search_input}':")
            sl.line_chart(data['Adj Close'])
        else:
            sl.write(f"No data found for '{search_input}'")

def get_suggestions(search_input):
                suggestions = difflib.get_close_matches(search_input, ticker_dict.keys())
                return suggestions

suggestions = get_suggestions(search_input)

def display_suggestions(suggestions):
                    if suggestions:
                        sl.write("Did you mean:")
                        for suggestion in suggestions:
                            if suggestion in ticker_dict.keys():
                                symbol = ticker_dict[suggestion]
                                data = yf.download(symbol, start, end)
                                if not data.empty:
                                    sl.write(f"{suggestion}: {symbol}")
                                    sl.line_chart(data['Adj Close'])
                                else:
                                    sl.write(f"No data found for '{suggestion}'")

display_suggestions(suggestions)