import axios from "axios";

const API_BASE = "http://127.0.0.1:8000";

export interface Activity {
  latitude: number;
  longitude: number;
  altitude: number;
}

export interface PredictionRequest {
  pm_type: string;
  temperature: number;
  humidity: number;
  pressure: number;
  wind_north: number;
  wind_east: number;
  latitude: number;
  longitude: number;
  altitude: number;
  activities: Activity[];
}

export interface PredictionResponse {
  pm_value: number;
  unit: string;
  pm_type: string;
}

export async function predictPM(
  payload: PredictionRequest
): Promise<PredictionResponse> {
  const res = await axios.post(`${API_BASE}/pm/predict`, payload);
  return res.data;
}
