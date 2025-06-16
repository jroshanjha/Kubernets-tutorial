from fastapi import FastAPI, Request
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    prediction = model.predict([data['features']])
    return {"prediction": prediction.tolist()}
