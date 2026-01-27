from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict

from ml.interface.feature_builder import build_features
from ml.interface.predict import predict_pm

router = APIRouter(prefix="/pm", tags=["PM Prediction"])


class PredictionRequest(BaseModel):
    pm_type: str  # pm1 | pm2_5 | pm10

    temperature: float
    humidity: float
    pressure: float

    wind_north: float
    wind_east: float

    latitude: float
    longitude: float
    altitude: float

    activities: List[Dict]  # [{latitude, longitude, altitude}]


class PredictionResponse(BaseModel):
    pm_value: float
    unit: str
    pm_type: str


@router.post("/predict", response_model=PredictionResponse)
def predict_pm_endpoint(payload: PredictionRequest):
    
    pm_value = predict_pm(payload)

    return {
        "pm_value": float(pm_value),
        "unit": "µg/m³",
        "pm_type": payload.pm_type,
    }

