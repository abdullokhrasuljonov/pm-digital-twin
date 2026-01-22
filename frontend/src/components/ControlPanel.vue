<script setup lang="ts">
import { computed } from "vue";
import { useEnvStore } from "../store/envStore";
import { usePMStore } from "../store/pmStore";
import { fetchPmData } from "../services/pmApi";

/* =========================
   Stores
========================= */
const env = useEnvStore();
const pmStore = usePMStore();

/* =========================
   PM selector (computed)
========================= */
type PMType = "pm1" | "pm2_5" | "pm10";

const selectedPM = computed<PMType>({
  get: () => pmStore.pmType,
  set: (val) => pmStore.setPMType(val),
});

/* =========================
   Actions
========================= */
async function runSimulation() {
  try {
    const res = await fetchPmData();
    console.log("Backend response:", res.data);
  } catch (err) {
    console.error("Simulation failed:", err);
  }
}
</script>

<template>
  <aside class="space-y-6 text-sm text-slate-200">
    <!-- Title -->
    <h3 class="text-base font-semibold text-white">
      Simulation Controls
    </h3>

    <!-- PM TYPE -->
    <div class="flex flex-col gap-1">
      <label class="text-sm font-medium whitespace-nowrap">
        PM Type
      </label>
      <select
        v-model="selectedPM"
        class="rounded-lg border border-slate-700 bg-slate-950 px-2 py-2 text-slate-200
               focus:outline-none focus:ring-2"
      >
        <option value="pm1">PM1.0</option>
        <option value="pm2_5">PM2.5</option>
        <option value="pm10">PM10</option>
      </select>
    </div>

    <!-- TIME RANGE -->
    <div class="flex flex-col gap-4">
      <div class="flex flex-col gap-1">
        <label class="text-sm font-medium text-slate-300">
          Start Time
        </label>
        <input
          type="datetime-local"
          v-model="env.timeRange.start"
          class="w-full rounded-lg border border-slate-700 bg-slate-950 px-2 py-2 text-slate-200
                 focus:outline-none focus:ring-2 focus:ring-sky-500"
        />
      </div>

      <div class="flex flex-col gap-1">
        <label class="text-sm font-medium text-slate-300">
          End Time
        </label>
        <input
          type="datetime-local"
          v-model="env.timeRange.end"
          class="w-full rounded-lg border border-slate-700 bg-slate-950 px-2 py-2 text-slate-200
                 focus:outline-none focus:ring-2 focus:ring-sky-500"
        />
      </div>
    </div>

    <!-- HUMIDITY -->
    <div class="flex flex-col gap-1">
      <label class="font-medium">
        Humidity
        <span class="text-slate-400">
          ({{ env.humidity }}%)
        </span>
      </label>
      <input
        type="range"
        min="0"
        max="100"
        step="1"
        v-model.number="env.humidity"
        class="w-full accent-sky-500"
      />
    </div>

    <!-- WIND SPEED -->
    <div class="flex flex-col gap-1">
      <label class="font-medium">
        Wind Speed
        <span class="text-slate-400">
          ({{ env.windSpeed }} m/s)
        </span>
      </label>
      <input
        type="range"
        min="0"
        max="20"
        step="0.5"
        v-model.number="env.windSpeed"
        class="w-full accent-sky-500"
      />
    </div>

    <!-- WIND DIRECTION -->
    <div class="flex flex-col gap-1">
      <label class="font-medium">
        Wind Direction
        <span class="text-slate-400">
          ({{ env.windDirection }}°)
        </span>
      </label>
      <input
        type="range"
        min="0"
        max="360"
        step="5"
        v-model.number="env.windDirection"
        class="w-full accent-sky-500"
      />
    </div>

    <!-- RUN BUTTON -->
    <button
      @click="runSimulation"
      class="w-full rounded-lg bg-sky-600 px-4 py-2 font-medium text-white
             hover:bg-sky-500 transition"
    >
      Run Simulation
    </button>
  </aside>
</template>
