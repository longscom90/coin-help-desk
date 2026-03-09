import requests
import pandas as pd
import os

BASE_URL = "https://fapi.binance.com/fapi/v1/klines"

symbols = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "XRPUSDT"
]

interval = "15m"
limit = 1000

SAVE_PATH = "D:\coding_Project\coin_help_desk\data"

os.makedirs(SAVE_PATH, exist_ok=True)


def collect_data(symbol):

    print(f"Downloading {symbol}")

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    df = pd.DataFrame(data)

    df = df.iloc[:, 0:6]
    df.columns = ["timestamp", "open", "high", "low", "close", "volume"]

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

    save_file = os.path.join(SAVE_PATH, f"{symbol}.csv")

    df.to_csv(save_file, index=False)

    print(f"Saved -> {save_file}")


def run():

    print("=== Coin Help Desk Data Collector ===")

    for symbol in symbols:
        collect_data(symbol)


if __name__ == "__main__":
    run()