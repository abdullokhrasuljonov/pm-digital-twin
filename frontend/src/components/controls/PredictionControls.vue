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
  <div class="space-y-4 p-4 bg-slate-900 rounded-xl text-black">

    <h2 class="text-xl font-semibold text-white">PM Prediction</h2>

    <!-- PM type -->
    <select v-model="pm_type" class="input">
      <option value="pm2_5">PM2.5</option>
      <option value="pm10">PM10</option>
      <option value="pm1">PM1</option>
    </select>

    <!-- Weather -->
    <div class="grid grid-cols-2 gap-2">
      <input v-model.number="temperature" type="number" class="input" placeholder="Temperature (°C)" />
      <input v-model.number="humidity" type="number" class="input" placeholder="Humidity (%)" />
      <input v-model.number="pressure" type="number" class="input" placeholder="Pressure (hPa)" />
    </div>

    <!-- Wind -->
    <div class="grid grid-cols-2 gap-2">
      <input v-model.number="wind_north" type="number" class="input" placeholder="Wind North" />
      <input v-model.number="wind_east" type="number" class="input" placeholder="Wind East" />
    </div>

    <!-- Location -->
    <div class="grid grid-cols-3 gap-2">
      <input v-model.number="latitude" type="number" class="input" placeholder="Latitude" />
      <input v-model.number="longitude" type="number" class="input" placeholder="Longitude" />
      <input v-model.number="altitude" type="number" class="input" placeholder="Altitude (m)" />
    </div>

    <!-- Activity -->
    <h3 class="text-sm text-slate-300">Activity source</h3>
    <div class="grid grid-cols-3 gap-2">
      <input v-model.number="activity_lat" type="number" class="input" placeholder="Lat" />
      <input v-model.number="activity_lon" type="number" class="input" placeholder="Lon" />
      <input v-model.number="activity_alt" type="number" class="input" placeholder="Alt" />
    </div>

    <!-- Button -->
    <button
      @click="runPrediction"
      :disabled="loading"
      class="px-4 py-2 bg-blue-600 hover:bg-blue-700 rounded"
    >
      {{ loading ? "Predicting..." : "Run Prediction" }}
    </button>

    <!-- Result -->
    <div v-if="result" class="mt-4 p-3 bg-slate-800 rounded">
      <p class="text-sm text-slate-400">
        PM Type: {{ result.pm_type }}
      </p>
      <p class="text-lg font-semibold text-white">
        Pedicted value: {{ result.pm_value.toFixed(2) }} {{ result.unit }}
      </p>
    </div>

    <!-- Error -->
    <p v-if="error" class="text-red-400">{{ error }}</p>

  </div>
</template>

