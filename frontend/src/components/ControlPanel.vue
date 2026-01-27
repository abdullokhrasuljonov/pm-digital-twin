<script setup lang="ts">
import { ref } from "vue";
import HistoricalControls from "./controls/HistoricalControls.vue";
import PredictionControls from "./controls/PredictionControls.vue";

const activeTab = ref<"history" | "prediction">("history");
</script>

<template>
  <div class="w-full text-slate-200">
    <!-- Tabs -->
    <div class="flex border-b border-slate-700 mb-4">
      <button
        class="px-4 py-2 text-sm font-medium"
        :class="activeTab === 'history'
          ? 'border-b-2 border-cyan-400 text-cyan-400'
          : 'text-slate-400 hover:text-slate-200'"
        @click="activeTab = 'history'"
      >
        Historical
      </button>

      <button
        class="px-4 py-2 text-sm font-medium ml-4"
        :class="activeTab === 'prediction'
          ? 'border-b-2 border-purple-400 text-purple-400'
          : 'text-slate-400 hover:text-slate-200'"
        @click="activeTab = 'prediction'"
      >
        Prediction
      </button>
    </div>

    <!-- Content -->
    <div>
      <HistoricalControls v-if="activeTab === 'history'" />
      <PredictionControls v-else />
    </div>
  </div>
</template>
