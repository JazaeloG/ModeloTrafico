from fastapi import FastAPI
from pydantic import BaseModel
import joblib

model = joblib.load("models/traffic_model.joblib")

app = FastAPI()

class InputData(BaseModel):
    DateTime: str 
    Junction: int

@app.post("/predict")
def predict_traffic(data: InputData):

    hour = int(data.DateTime.split(":")[0])

    
    predicted_junction = model.predict([[hour, data.Junction]])

    is_traffic = bool(predicted_junction[0])

    return {"is_traffic": is_traffic}

## No habra trafico  {"DateTime": "05:00:00","Junction": 2}
## Si habra trafico {"DateTime": "03:00:00","Junction": 1}