<script setup lang="ts">
import { ref } from "vue";
import { predictPM } from "../../services/pmPredictionApi";
import type { PredictionResponse } from "../../services/pmPredictionApi";

const loading = ref(false);
const error = ref<string | null>(null);
const result = ref<PredictionResponse | null>(null);

/* --- Form state --- */
const pm_type = ref<"pm2_5" | "pm10" | "pm1">("pm2_5");

const temperature = ref(20);
const humidity = ref(60);
const pressure = ref(1013);

const wind_north = ref(1.2);
const wind_east = ref(0.8);

const latitude = ref(35.1);
const longitude = ref(129.0);
const altitude = ref(15);

const activity_lat = ref(35.101);
const activity_lon = ref(129.001);
const activity_alt = ref(10);

/* --- Run prediction --- */
async function runPrediction() {
  loading.value = true;
  error.value = null;

  try {
    result.value = await predictPM({
      pm_type: pm_type.value,
      temperature: temperature.value,
      humidity: humidity.value,
      pressure: pressure.value,
      wind_north: wind_north.value,
      wind_east: wind_east.value,
      latitude: latitude.value,
      longitude: longitude.value,
      altitude: altitude.value,
      activities: [
        {
          latitude: activity_lat.value,
          longitude: activity_lon.value,
          altitude: activity_alt.value,
        },
      ],
    });
  } catch (e: any) {
    error.value = e.message ?? "Prediction failed";
  } finally {
    loading.value = false;
  }
}
</script>


<template>
    <div class="space-y-4">
        <div class="space-y-6 p-4 bg-slate-900 rounded-xl text-slate-200 text-sm">
          <!-- ========================= -->
          <!-- PM Characteristics -->
          <!-- ========================= -->
          <div class="space-y-3">
            <div class="flex items-center gap-2 text-slate-300 font-medium">
              <span class="w-1 h-4 bg-purple-500 rounded-full"></span>
              PM Characteristics
            </div>
        
            <!-- PM Type -->
            <div class="grid grid-cols-[1fr_auto] items-center gap-x-4">
              <label>PM type</label>
              <select v-model="pm_type" class="input w-[80px] text-slate-800 px-2 py-1 rounded-lg">
                <option value="pm2_5">PM2.5</option>
                <option value="pm10">PM10</option>
                <option value="pm1">PM1</option>
              </select>
            </div>
          </div>    
        </div>
    
        <div class="space-y-6 p-4 bg-slate-900 rounded-xl text-slate-200 text-sm">
          <!-- ========================= -->
          <!-- Environmental Factors -->
          <!-- ========================= -->
          <div class="space-y-3">
            <div class="flex items-center gap-2 text-slate-300 font-medium">
              <span class="w-1 h-4 bg-purple-500 rounded-full"></span>
              Environmental Factors
            </div>
        
            <div class="grid grid-cols-[1fr_auto] items-center gap-x-4">
              <label>Temperature (°C)</label>
              <input v-model.number="temperature" type="number" class="input w-[80px] text-slate-800 px-2 py-1 rounded-lg" />
            </div>
        
            <div class="grid grid-cols-[1fr_auto] items-center gap-x-4">
              <label>Humidity (%)</label>
              <input v-model.number="humidity" type="number" class="input w-[80px] text-slate-800 px-2 py-1 rounded-lg" />
            </div>
        
            <div class="grid grid-cols-[1fr_auto] items-center gap-x-4">
              <label>Pressure (hPa)</label>
              <input v-model.number="pressure" type="number" class="input w-[80px] text-slate-800 px-2 py-1 rounded-lg" />
            </div>
        
            <div class="grid grid-cols-[1fr_auto] items-center gap-x-4">
              <label>Wind North (m/s)</label>
              <input v-model.number="wind_north" type="number" class="input w-[80px] text-slate-800 px-2 py-1 rounded-lg" />
            </div>
        
            <div class="grid grid-cols-[1fr_auto] items-center gap-x-4">
              <label>Wind East (m/s)</label>
              <input v-model.number="wind_east" type="number" class="input w-[80px] text-slate-800 px-2 py-1 rounded-lg" />
            </div>
          </div>
        
        </div>


        <div class="space-y-6 p-4 bg-slate-900 rounded-xl text-slate-200 text-sm">
          <!-- ========================= -->
          <!-- Geolocations -->
          <!-- ========================= -->
          <div class="space-y-3">
            <div class="flex items-center gap-2 text-slate-300 font-medium">
              <span class="w-1 h-4 bg-purple-500 rounded-full"></span>
              Geolocations
            </div>
        
            <div class="grid grid-cols-[1fr_auto] items-center gap-x-4">
              <label>Latitude</label>
              <input v-model="latitude" type="number" class="input w-[80px] text-slate-800 px-2 py-1 rounded-lg" />
            </div>
        
            <div class="grid grid-cols-[1fr_auto] items-center gap-x-4">
              <label>Longitude</label>
              <input v-model="longitude" type="number" class="input w-[80px] text-slate-800 px-2 py-1 rounded-lg" />
            </div>
        
            <div class="grid grid-cols-[1fr_auto] items-center gap-x-4">
              <label>Altitude</label>
              <input v-model="altitude" type="number" class="input w-[80px] text-slate-800 px-2 py-1 rounded-lg" />
            </div>
        
            <div class="grid grid-cols-[1fr_auto] items-center gap-x-4">
              <label>Activity latitude</label>
              <input v-model="activity_lat" type="number" class="input w-[80px] text-slate-800 px-2 py-1 rounded-lg" />
            </div>
        
            <div class="grid grid-cols-[1fr_auto] items-center gap-x-4">
              <label>Activity longitude</label>
              <input v-model="activity_lon" type="number" class="input w-[80px] text-slate-800 px-2 py-1 rounded-lg" />
            </div>

            <div class="grid grid-cols-[1fr_auto] items-center gap-x-4">
              <label>Activity altitude</label>
              <input v-model="activity_alt" type="number" class="input w-[80px] text-slate-800 px-2 py-1 rounded-lg" />
            </div>
          </div>
        
          <!-- ========================= -->
          <!-- Action -->
          <!-- ========================= -->
          <button
            @click="runPrediction"
            :disabled="loading"
            class="w-full mt-2 bg-blue-600 hover:bg-blue-700 py-2 rounded-lg text-white font-medium disabled:opacity-60"
          >
            {{ loading ? "Predicting..." : "Run Prediction" }}
          </button>
        
          <!-- ========================= -->
          <!-- Result -->
          <!-- ========================= -->
          <div v-if="result" class="mt-3 p-3 bg-slate-800 rounded-lg">
            <p class="text-xs text-slate-400">PM Type</p>
            <p class="text-white font-semibold">
              {{ result.pm_type }} — {{ result.pm_value.toFixed(2) }} {{ result.unit }}
            </p>
          </div>
        
          <p v-if="error" class="text-red-400 text-sm">{{ error }}</p>
        </div>
        
    </div>


</template>



