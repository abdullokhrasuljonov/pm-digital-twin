from pydantic import BaseModel
from typing import Optional

class PMPredictionInput(BaseModel):
    pm_type: str               # pm1 | pm2_5 | pm10
    temperature: float
    humidity: float
    wind_speed: float
    wind_direction: float
    latitude: float
    longitude: float
    altitude: float
    hour: int
