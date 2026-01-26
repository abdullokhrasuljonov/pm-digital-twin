import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODELS = {
    "pm1": joblib.load(BASE_DIR / "XGBoost_PM1.pkl"),
    "pm2_5": joblib.load(BASE_DIR / "XGBoost_PM2_5.pkl"),
    "pm10": joblib.load(BASE_DIR / "XGBoost_PM10.pkl"),
}

def get_model(pm_type: str):
    if pm_type not in MODELS:
        raise ValueError(f"Unsupported PM type: {pm_type}")
    return MODELS[pm_type]
