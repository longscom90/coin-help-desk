import pandas as pd
import numpy as np
import os

DATA_PATH = "D:/coding_Project/coin_help_desk/data/features"
SAVE_PATH = "D:/coding_Project/coin_help_desk/dataset"

WINDOW_SIZE = 50

os.makedirs(SAVE_PATH, exist_ok=True)


def build_dataset(file):

    print("Processing:", file)

    df = pd.read_csv(f"{DATA_PATH}/{file}")

    features = df.drop(columns=["timestamp"]).values

    X = []
    y = []

    for i in range(WINDOW_SIZE, len(features) - 1):

        X.append(features[i-WINDOW_SIZE:i])

        if features[i+1][3] > features[i][3]:
            y.append(1)
        else:
            y.append(0)

    X = np.array(X)
    y = np.array(y)

    symbol = file.replace(".csv", "")

    np.save(f"{SAVE_PATH}/{symbol}_X.npy", X)
    np.save(f"{SAVE_PATH}/{symbol}_y.npy", y)

    print("Saved:", symbol)


def run():

    print("=== Coin Help Desk Dataset Builder ===")

    files = os.listdir(DATA_PATH)

    for file in files:

        if file.endswith(".csv"):
            build_dataset(file)


if __name__ == "__main__":
    run()