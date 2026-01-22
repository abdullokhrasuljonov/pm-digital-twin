import axios from "axios";
import { useEnvStore } from "../store/envStore";
import { usePMStore } from "../store/pmStore";

const API_BASE = "http://localhost:8000";

export async function fetchPmData() {
  const env = useEnvStore();
  const pm = usePMStore();

  // 🔍 debug (VERY IMPORTANT)
  console.log("API params:", {
    pm_type: pm.pmType,
    start_time: env.timeRange.start,
    end_time: env.timeRange.end,
  });

  return axios.get(`${API_BASE}/api/pm-data`, {
    params: {
      pm_type: pm.pmType,
      start_time: env.timeRange.start,
      end_time: env.timeRange.end,
      humidity: env.humidity,
      wind_speed: env.windSpeed,
    },
  });
}
