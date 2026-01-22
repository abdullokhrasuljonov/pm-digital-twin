from influxdb_client import InfluxDBClient
import os
from dotenv import load_dotenv

load_dotenv()

client = InfluxDBClient(
    url=os.getenv("INFLUX_URL"),
    token=os.getenv("INFLUX_TOKEN"),
    org=os.getenv("INFLUX_ORG"),
)

query_api = client.query_api()
