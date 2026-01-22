# from fastapi import FastAPI, Query
# from influxdb_client import InfluxDBClient
# from dotenv import load_dotenv
# import os

# # ==============================
# # Load environment variables
# # ==============================
# load_dotenv()

# INFLUX_URL = os.getenv("INFLUX_URL")
# INFLUX_TOKEN = os.getenv("INFLUX_TOKEN")
# INFLUX_ORG = os.getenv("INFLUX_ORG")
# INFLUX_BUCKET = os.getenv("INFLUX_BUCKET")

# HOST = os.getenv("BACKEND_HOST", "127.0.0.1")
# PORT = int(os.getenv("BACKEND_PORT", 3001))

# # ==============================
# # FastAPI App
# # ==============================
# app = FastAPI(title="PM Digital Twin Backend")

# # ==============================
# # InfluxDB Client
# # ==============================
# client = InfluxDBClient(
#     url=INFLUX_URL,
#     token=INFLUX_TOKEN,
#     org=INFLUX_ORG
# )

# query_api = client.query_api()

# # ==============================
# # API Endpoint
# # ==============================
# @app.get("/pm")
# def get_pm_data(
#     pm_type: str = Query("pm1"),
#     start: str = Query("2026-10-01T14:00:00Z"),
#     stop: str = Query("2026-10-01T16:00:00Z")
# ):
#     query = f'''
# from(bucket: "{INFLUX_BUCKET}")
#   |> range(start: time(v: "{start}"), stop: time(v: "{stop}"))
#   |> filter(fn: (r) =>
#       r._field == "{pm_type}" or
#       r._field == "latitude" or
#       r._field == "longitude" or
#       r._field == "altitude"
#   )
#   |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
# '''

#     tables = query_api.query(query)
#     data = []

#     for table in tables:
#         for record in table.records:
#             data.append(record.values)

#     return data


# @app.get("/")
# def health():
#     return {"status": "PM Digital Twin Backend is running"}

from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Query
from typing import Literal
from datetime import datetime

from influx_client import query_api
import os

app = FastAPI()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


BUCKET = os.getenv("INFLUX_BUCKET")
ORG = os.getenv("INFLUX_ORG")


@app.get("/api/pm-data")
def get_pm_data(
    pm_type: Literal["pm1", "pm2_5", "pm10"] = Query(...),
    start_time: datetime = Query(...),
    end_time: datetime = Query(...),
    humidity: float | None = Query(None, ge=0, le=100),
    wind_speed: float | None = Query(None, ge=0),
):
    """
    Receives parameters from frontend and queries InfluxDB
    """

    flux_query = f"""
    from(bucket: "{BUCKET}")
      |> range(
          start: time(v: "{start_time.isoformat()}Z"),
          stop: time(v: "{end_time.isoformat()}Z")
      )
      |> filter(fn: (r) =>
          r._measurement == "pm_50m_shift" and
          (
            r._field == "{pm_type}" or
            r._field == "latitude" or
            r._field == "longitude" or
            r._field == "altitude"
          )
      )
      |> pivot(
          rowKey: ["_time"],
          columnKey: ["_field"],
          valueColumn: "_value"
      )
      |> keep(columns: ["_time", "{pm_type}", "latitude", "longitude", "altitude"])
    """


    tables = query_api.query(flux_query, org=ORG)

    results = []

    for table in tables:
        for record in table.records:
            results.append({
                "time": record.get_time(),
                "value": record.values.get(pm_type),
                "latitude": record.values.get("latitude"),
                "longitude": record.values.get("longitude"),
                "altitude": record.values.get("altitude"),
            })

    return {
        "pm_type": pm_type,
        "start_time": start_time,
        "end_time": end_time,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "count": len(results),
        "data": results,
    }

