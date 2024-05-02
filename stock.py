
import yfinance as yf
import streamlit as sl
import pandas as pd
import seaborn as sns

sl.title('My little Finance App')
df = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers = df.Symbol.to_list()
dropdown = sl.multiselect('Choose your  ticker', tickers)

start = sl.date_input('Start date', pd.to_datetime('2019-01-01'))
end = sl.date_input('End date', pd.to_datetime('today'))



if len(dropdown) > 0:
    df = (yf.download(dropdown, start, end)['Adj Close'])
    sl.line_chart(df)



    import matplotlib.pyplot as plt

    data = {'Category': ['A', 'B', 'C', 'D'], 'Value': [1, 1, 1, 1]}
    df = pd.DataFrame(data)

    plt.figure(figsize=(6, 6))
    sns.set_palette("Set3")
    sns.set_style("whitegrid")
    plt.title("Pie Chart")
    plt.pie(df['Value'], labels=df['Category'], autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()