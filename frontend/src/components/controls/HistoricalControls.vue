<script setup lang="ts">
import { useEnvStore } from "../../store/envStore";
const env = useEnvStore();
</script>

<template>
  <div class="space-y-6">

    <!-- ================= PM Characteristics ================= -->
    <div class="bg-slate-900 rounded-xl p-4 space-y-3">
      <div class="flex items-center gap-2 text-slate-200 text-sm font-medium">
        <span class="w-1 h-4 bg-purple-500 rounded"></span>
        PM Characteristics
      </div>

      <div class="grid grid-cols-[1fr_auto] items-center gap-x-4">
        <label class="text-slate-300 text-sm">PM Type</label>
        <select
          v-model="env.pmType"
          class="input w-[80px] text-slate-800 px-2 py-1 rounded-lg text-sm"
        >
          <option value="pm2_5">PM2.5</option>
          <option value="pm10">PM10</option>
          <option value="pm1">PM1</option>
        </select>
      </div>
    </div>

    <!-- ================= Time Range ================= -->
    <div class="bg-slate-900 rounded-xl p-4 space-y-3">
      <div class="flex items-center gap-2 text-slate-200 text-sm font-medium">
        <span class="w-1 h-4 bg-purple-500 rounded"></span>
        Time Range
      </div>

      <div class="grid grid-cols-[1fr_auto] items-center gap-3">
        <label class="text-slate-300 text-sm">Start Time</label>
        <input
          type="datetime-local"
          v-model="env.timeRange.start"
          class="input w-[160px] text-sm px-2 py-1 text-slate-800 rounded-md"
        />
      </div>

      <div class="grid grid-cols-[1fr_auto] items-center gap-3">
        <label class="text-slate-300 text-sm">End Time</label>
        <input
          type="datetime-local"
          v-model="env.timeRange.end"
          class="input w-[160px] text-sm px-2 py-1 text-slate-800 rounded-md"
        />
      </div>
    </div>

    <!-- ================= Environmental Factors ================= -->
    <div class="bg-slate-900 rounded-xl p-4 space-y-3">
      <div class="flex items-center gap-2 text-slate-200 text-sm font-medium">
        <span class="w-1 h-4 bg-purple-500 rounded"></span>
        Environmental Factors
      </div>

      <div class="grid grid-cols-[1fr_auto] items-center gap-x-4">
        <label class="text-slate-300 text-sm">Humidity (%)</label>
        <input
          type="number"
          min="0"
          max="100"
          v-model.number="env.humidity"
          class="input w-[80px] text-slate-800 px-2 py-1 rounded-lg text-sm"
        />
      </div>

      <div class="grid grid-cols-[1fr_auto] items-center gap-3">
        <label class="text-slate-300 text-sm">Wind Speed (m/s)</label>
        <input
          type="number"
          min="0"
          step="0.1"
          v-model.number="env.windSpeed"
          class="input w-[80px] text-slate-800 px-2 py-1 rounded-lg text-sm"
        />
      </div>

      <div class="grid grid-cols-[1fr_auto] items-center gap-3">
        <label class="text-slate-300 text-sm">Wind Direction (°)</label>
        <input
          type="number"
          min="0"
          max="360"
          step="1"
          v-model.number="env.windDirection"
          class="input w-[80px] text-slate-800 px-2 py-1 rounded-lg text-sm"
        />
      </div>
    </div>

          <!-- ========================= -->
          <!-- Action -->
          <!-- ========================= -->
          <button
            @click=""

            class="w-full mt-2 bg-blue-600 hover:bg-blue-700 py-2 rounded-lg text-white font-medium disabled:opacity-60"
          >
            Visualize
          </button>

  </div>
</template>

