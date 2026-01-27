<script setup lang="ts">
import { useEnvStore } from "../../store/envStore";
const env = useEnvStore();
</script>

<template>
  <div class="space-y-4">
    <div>
      <label class="block text-xs mb-1">Start Time</label>
      <input type="datetime-local" v-model="env.timeRange.start"
        class="w-full bg-slate-900 border border-slate-700 rounded px-2 py-1" />
    </div>

    <div>
      <label class="block text-xs mb-1">End Time</label>
      <input type="datetime-local" v-model="env.timeRange.end"
        class="w-full bg-slate-900 border border-slate-700 rounded px-2 py-1" />
    </div>

    <div>
      <label class="block text-xs mb-1">Humidity (%)</label>
      <input type="range" min="0" max="100" v-model.number="env.humidity" />
      <div class="text-xs text-slate-400">{{ env.humidity }}%</div>
    </div>

    <div>
      <label class="block text-xs mb-1">Wind Speed (m/s)</label>
      <input type="range" min="0" max="20" step="0.5"
        v-model.number="env.windSpeed" />
    </div>

    <div>
      <label class="block text-xs mb-1">Wind Direction (°)</label>
      <input type="range" min="0" max="360" step="5"
        v-model.number="env.windDirection" />
    </div>
  </div>
</template>
