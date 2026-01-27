from ml.interface.predict import predict_pm
from ml.interface.schema import PMPredictionInput

if __name__ == "__main__":
    data = PMPredictionInput(
        pm_type="pm2_5",
        temperature=10.5,
        humidity=32.0,
        pressure=1018.0,
        wind_north=1.2,
        wind_east=-0.5,
        latitude=35.0879,
        longitude=128.7929,
        altitude=50.0,
        activities=[
            {"latitude": 35.08805, "longitude": 128.79291, "altitude": 0},
            {"latitude": 35.08794, "longitude": 128.79291, "altitude": 0},
        ],
    )

    pm_value = predict_pm(data)
    print("Predicted PM:", pm_value)
