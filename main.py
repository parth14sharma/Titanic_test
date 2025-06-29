# main.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load model
model = joblib.load("titanic_model.pkl")

# Define input schema
class Passenger(BaseModel):
    Pclass: int
    Sex: int     # 0 = male, 1 = female
    Age: float

@app.post("/predict")
def predict_survival(passenger: Passenger):
    data = np.array([[passenger.Pclass, passenger.Sex, passenger.Age]])
    prediction = model.predict(data)
    return {"survived": int(prediction[0])}

