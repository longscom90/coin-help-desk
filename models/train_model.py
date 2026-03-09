import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

X = np.load("D:/coding_Project/coin_help_desk/dataset/BTCUSDT_X.npy")
y = np.load("D:/coding_Project/coin_help_desk/dataset/BTCUSDT_y.npy")

model = Sequential()

model.add(LSTM(64, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(32, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.fit(X, y, epochs=10, batch_size=32)

model.save("btc_model.h5")