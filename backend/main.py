from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from backend.routers.pm_data import router as pm_data_router
from backend.routers.pm_predict import router as pm_predict_router

load_dotenv()

app = FastAPI(title="PM Monitoring Digital Twin API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pm_data_router)
app.include_router(pm_predict_router)
