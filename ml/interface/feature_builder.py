import numpy as np
from .schema import PMPredictionInput

def build_features(data: PMPredictionInput) -> np.ndarray:
    return np.array([[
        data.temperature,
        data.humidity,
        data.wind_speed,
        data.wind_direction,
        data.latitude,
        data.longitude,
        data.altitude,
        data.hour,
    ]])
