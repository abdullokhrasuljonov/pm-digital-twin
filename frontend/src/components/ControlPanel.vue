<script setup lang="ts">
import { useEnvStore } from "../store/envStore";

const env = useEnvStore();
</script>

<template>
  <div class="control-panel">
    <h3>Simulation Controls</h3>

    <!-- Time range -->
    <div class="group">
      <label>Start Time</label>
      <input type="datetime-local" v-model="env.timeRange.start" />
    </div>

    <div class="group">
      <label>End Time</label>
      <input type="datetime-local" v-model="env.timeRange.end" />
    </div>

    <!-- Humidity -->
    <div class="group">
      <label>Humidity (%)</label>
      <input
        type="range"
        min="0"
        max="100"
        step="1"
        v-model.number="env.humidity"
      />
      <span>{{ env.humidity }}%</span>
    </div>

    <!-- Wind speed -->
    <div class="group">
      <label>Wind Speed (m/s)</label>
      <input
        type="range"
        min="0"
        max="20"
        step="0.5"
        v-model.number="env.windSpeed"
      />
      <span>{{ env.windSpeed }} m/s</span>
    </div>

    <!-- Wind direction -->
    <div class="group">
      <label>Wind Direction (°)</label>
      <input
        type="range"
        min="0"
        max="360"
        step="5"
        v-model.number="env.windDirection"
      />
      <span>{{ env.windDirection }}°</span>
    </div>
  </div>
</template>

<style scoped>
.control-panel {
  background: #020617;
  color: white;
}

.group {
  display: flex;
  flex-direction: column;
  margin-bottom: 12px;
}

input[type="range"] {
  width: 100%;
}
</style>
