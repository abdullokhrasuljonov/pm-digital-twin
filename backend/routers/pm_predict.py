from fastapi import APIRouter, HTTPException
from ml.interface.predict import predict_pm
from ml.interface.schema import PMPredictionInput

router = APIRouter(prefix="/api", tags=["PM Prediction"])

@router.post("/predict")
def predict(data: PMPredictionInput):
    try:
        return {
            "pm_type": data.pm_type,
            "predicted_pm": predict_pm(data),
            "unit": "µg/m³",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
