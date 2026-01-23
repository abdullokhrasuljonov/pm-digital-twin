from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Literal
from datetime import datetime
from dotenv import load_dotenv
import os

from influx_client import query_api
from geo_utils import latlon_to_xyz

# --------------------------------------------------
# Environment
# --------------------------------------------------
load_dotenv()

INFLUX_BUCKET = os.getenv("INFLUX_BUCKET")
INFLUX_ORG = os.getenv("INFLUX_ORG")

# --------------------------------------------------
# FastAPI app
# --------------------------------------------------
app = FastAPI(title="PM Monitoring Digital Twin API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# API Endpoint
# --------------------------------------------------
@app.get("/api/pm-data")
def get_pm_data(
    pm_type: Literal["pm1", "pm2_5", "pm10"] = Query(...),
    start_time: datetime = Query(...),
    end_time: datetime = Query(...),
    humidity: float | None = Query(None, ge=0, le=100),
    wind_speed: float | None = Query(None, ge=0),
):
    """
    Retrieve spatial PM data from InfluxDB and convert it
    into local Cartesian coordinates for digital-twin rendering.
    """

    # --------------------------------------------------
    # Flux query (pivoted for spatial alignment)
    # --------------------------------------------------
    flux_query = f"""
    from(bucket: "{INFLUX_BUCKET}")
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

    tables = query_api.query(flux_query, org=INFLUX_ORG)

    raw_points = []

    for table in tables:
        for record in table.records:
            raw_points.append({
                "time": record.get_time(),
                "value": record.values.get(pm_type),
                "latitude": record.values.get("latitude"),
                "longitude": record.values.get("longitude"),
                "altitude": record.values.get("altitude"),
            })

    # --------------------------------------------------
    # Convert lat/lon → local XYZ
    # --------------------------------------------------
    xyz_points = []

    if raw_points:
        # Reference origin (first valid point)
        lat0 = raw_points[0]["latitude"]
        lon0 = raw_points[0]["longitude"]
        alt0 = raw_points[0]["altitude"]

        for p in raw_points:
            x, y, z = latlon_to_xyz(
                p["latitude"],
                p["longitude"],
                p["altitude"],
                lat0,
                lon0,
                alt0,
            )

            xyz_points.append({
                "time": p["time"],
                "x": x,
                "y": y,
                "z": z,
                "value": p["value"],
            })

    # --------------------------------------------------
    # Response
    # --------------------------------------------------
    return {
        "pm_type": pm_type,
        "start_time": start_time,
        "end_time": end_time,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "count": len(xyz_points),
        "data": xyz_points,
    }
