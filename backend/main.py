from fastapi import FastAPI, Query
from influxdb_client import InfluxDBClient
from dotenv import load_dotenv
import os

# ==============================
# Load environment variables
# ==============================
load_dotenv()

INFLUX_URL = os.getenv("INFLUX_URL")
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN")
INFLUX_ORG = os.getenv("INFLUX_ORG")
INFLUX_BUCKET = os.getenv("INFLUX_BUCKET")

HOST = os.getenv("BACKEND_HOST", "127.0.0.1")
PORT = int(os.getenv("BACKEND_PORT", 3001))

# ==============================
# FastAPI App
# ==============================
app = FastAPI(title="PM Digital Twin Backend")

# ==============================
# InfluxDB Client
# ==============================
client = InfluxDBClient(
    url=INFLUX_URL,
    token=INFLUX_TOKEN,
    org=INFLUX_ORG
)

query_api = client.query_api()

# ==============================
# API Endpoint
# ==============================
@app.get("/pm")
def get_pm_data(
    pm_type: str = Query("pm1"),
    start: str = Query("2026-10-01T14:00:00Z"),
    stop: str = Query("2026-10-01T16:00:00Z")
):
    query = f'''
from(bucket: "{INFLUX_BUCKET}")
  |> range(start: time(v: "{start}"), stop: time(v: "{stop}"))
  |> filter(fn: (r) =>
      r._field == "{pm_type}" or
      r._field == "latitude" or
      r._field == "longitude" or
      r._field == "altitude"
  )
  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
'''

    tables = query_api.query(query)
    data = []

    for table in tables:
        for record in table.records:
            data.append(record.values)

    return data


@app.get("/")
def health():
    return {"status": "PM Digital Twin Backend is running"}
