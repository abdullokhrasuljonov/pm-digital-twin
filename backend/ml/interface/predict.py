from .schema import PMPredictionInput
from .feature_builder import build_features
from ml.model.loader import get_model

def predict_pm(input_data: PMPredictionInput) -> float:
    model = get_model(input_data.pm_type)
    features = build_features(input_data)
    return float(model.predict(features)[0])
