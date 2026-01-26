from pydantic import BaseModel
from typing import List, Dict

class PMPredictionInput(BaseModel):
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
