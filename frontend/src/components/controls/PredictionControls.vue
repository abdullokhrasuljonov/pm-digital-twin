<script setup lang="ts">
import { ref } from "vue";
import { predictPM } from "../../services/pmPredictionApi";
import type { PredictionResponse } from "../../services/pmPredictionApi";

const loading = ref(false);
const error = ref<string | null>(null);
const result = ref<PredictionResponse | null>(null);

async function runPrediction() {
  loading.value = true;
  error.value = null;

  try {
    result.value = await predictPM({
      pm_type: "pm2_5",
      temperature: 20,
      humidity: 60,
      pressure: 1013,
      wind_north: 1.2,
      wind_east: 0.8,
      latitude: 35.1,
      longitude: 129.0,
      altitude: 15,
      activities: [
        {
          latitude: 35.101,
          longitude: 129.001,
          altitude: 10,
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
  <div class="space-y-4 p-4 bg-slate-900 rounded-xl text-white">
    <h2 class="text-xl font-semibold">PM Prediction</h2>

    <!-- Run button -->
    <button
      @click="runPrediction"
      class="px-4 py-2 bg-blue-600 hover:bg-blue-700 rounded-lg"
      :disabled="loading"
    >
      {{ loading ? "Predicting..." : "Run Prediction" }}
    </button>

    <!-- Error -->
    <p v-if="error" class="text-red-400">{{ error }}</p>

    <!-- Result -->
    <div
      v-if="result"
      class="mt-4 p-4 rounded-lg bg-slate-800 border border-slate-700"
    >
      <p class="text-sm text-slate-400">
        PM Type: <span class="text-white">{{ result.pm_type }}</span>
      </p>

      <p class="text-3xl font-bold mt-2">
        {{ result.pm_value.toFixed(1) }}
        <span class="text-lg font-normal">{{ result.unit }}</span>
      </p>
    </div>
  </div>
</template>
