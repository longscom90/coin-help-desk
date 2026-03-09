from fastapi import FastAPI
import tensorflow as tf
import numpy as np
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "btc_model.h5")

model = tf.keras.models.load_model(MODEL_PATH)

@app.get("/predict")
def predict():

    dummy = np.random.rand(1,50,12)

    pred = model.predict(dummy)

    return {
        "coin": "BTC",
        "up_probability": float(pred[0][0])
    }