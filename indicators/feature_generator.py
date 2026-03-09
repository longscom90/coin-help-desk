import pandas as pd
import ta
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "features")

os.makedirs(OUTPUT_PATH, exist_ok=True)


def generate(file):

    df = pd.read_csv(os.path.join(DATA_PATH, file))

    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)

    df["rsi"] = ta.momentum.RSIIndicator(df["close"]).rsi()

    df["ema20"] = ta.trend.EMAIndicator(df["close"],20).ema_indicator()
    df["ema50"] = ta.trend.EMAIndicator(df["close"],50).ema_indicator()

    macd = ta.trend.MACD(df["close"])

    df["macd"] = macd.macd()
    df["macd_signal"] = macd.macd_signal()

    bb = ta.volatility.BollingerBands(df["close"])

    df["bb_high"] = bb.bollinger_hband()
    df["bb_low"] = bb.bollinger_lband()

    df.dropna(inplace=True)

    df.to_csv(os.path.join(OUTPUT_PATH,file),index=False)


def run():

    files = os.listdir(DATA_PATH)

    for f in files:

        if f.endswith(".csv"):

            generate(f)


if __name__ == "__main__":

    run()