<script setup lang="ts">
import { reactive } from "vue";

const form = reactive({
  pm_type: "pm2_5",

  temperature: 20,
  humidity: 60,
  pressure: 1013,

  wind_north: 1.5,
  wind_east: 0.8,

  latitude: 35.1,
  longitude: 129.0,
  altitude: 15,

  activities: [
    { latitude: 35.101, longitude: 129.001, altitude: 10 }
  ],
});

function submitPrediction() {
  console.log("Prediction payload", form);

  // 🔜 POST → /pm/predict
}
</script>

<template>
  <div class="space-y-4">
    <!-- PM Type -->
    <div>
      <label class="block text-md mb-1">PM Type</label>
      <select v-model="form.pm_type"
        class="w-full bg-slate-900 border border-slate-700 rounded px-2 py-1 text-sm">
        <option value="pm1">PM1.0</option>
        <option value="pm2_5">PM2.5</option>
        <option value="pm10">PM10</option>
      </select>
    </div>

    <!-- Weather -->
    <div class="grid grid-cols-2 gap-3">
      <input v-model.number="form.temperature" placeholder="Temp (°C)" class="input" />
      <input v-model.number="form.humidity" placeholder="Humidity (%)" class="input" />
      <input v-model.number="form.pressure" placeholder="Pressure (hPa)" class="input" />
    </div>

    <!-- Wind -->
    <div class="grid grid-cols-2 gap-3">
      <input v-model.number="form.wind_north" placeholder="Wind North (m/s)" class="input" />
      <input v-model.number="form.wind_east" placeholder="Wind East (m/s)" class="input" />
    </div>

    <!-- Location -->
    <div class="grid grid-cols-3 gap-3">
      <input v-model.number="form.latitude" placeholder="Lat" class="input" />
      <input v-model.number="form.longitude" placeholder="Lon" class="input" />
      <input v-model.number="form.altitude" placeholder="Alt (m)" class="input" />
    </div>

    <button
      @click="submitPrediction"
      class="w-full bg-purple-600 hover:bg-purple-500 text-white text-sm py-2 rounded">
      Run Prediction
    </button>
  </div>
</template>

<style scoped>
.input {
  background: #020617;
  border: 1px solid #334155;
  border-radius: 6px;
  padding: 4px 6px;
  font-size: 14px;
  color: white;
}
</style>
