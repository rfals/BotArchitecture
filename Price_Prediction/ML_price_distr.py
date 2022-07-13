from binance import Client
import pandas as pd

api_key = "api_key"

secret_key = "api_secret"

client = Client(api_key = api_key, api_secret = secret_key, tld = "com")

def get_history(symbol, interval, start, end = None):
    bars = client.get_historical_klines(symbol = symbol, interval = interval,
                                       start_str = start, end_str = end, limit = 1000)
    df = pd.DataFrame(bars)
    df["Date"] = pd.to_datetime(df.iloc[:,0], unit = "ms")
    df.columns = ["Open Time", "Open", "High", "Low", "Close", "Volume", "Close Time",
             "Quote Asset Volume", "Number of Trades", "Taker Buy Base Asset Volume",
             "Taker Buy Quote Asset Volume", "Ignore", "Date"]
    df = df[["Date","Open", "High", "Low", "Close", "Volume" ]].copy()
    df.set_index("Date", inplace = True)
    for column in df.columns:
        df[column] = pd.to_numeric(df[column], errors = "coerce")
    return df


df = get_history(symbol = "ETHBTC", interval = "1m", start = "1 month ago UTC")
df

# download csv

df.to_csv("ETHBTC.csv")
