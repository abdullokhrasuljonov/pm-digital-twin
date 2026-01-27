from pydantic import BaseModel
from typing import List

class Activity(BaseModel):
    latitude: float
    longitude: float
    altitude: float

class PMPredictionInput(BaseModel):
    pm_type: str  # pm1 | pm25 | pm10

    temperature: float
    humidity: float
    pressure: float

    wind_north: float
    wind_east: float

    latitude: float
    longitude: float
    altitude: float

    activities: List[Activity]
